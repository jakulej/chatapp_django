# chat/consumers.py
import json
import datetime

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer 
from .models import Room, Message


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        self.user = self.scope["user"]
        if self.user.rooms.filter(id=self.room_name).exists():
            async_to_sync(self.channel_layer.group_add)(
                self.room_group_name, self.channel_name
            )
            self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        print(message)
        self.save_message(message)
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
                self.room_group_name, {
                    "type": "chat.message", 
                    "message": message, 
                    "user" : self.user.username
                    }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]
        user = event["user"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            "message": message,
            "user" : user
            }))
    
    def save_message(self, content):
        time = datetime.datetime.now()
        room_obj = Room.objects.get(id=self.room_name)
        message = Message(sender=self.user, room=room_obj, content=content, timestamp=time)
        message.save()

