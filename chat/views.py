from django.shortcuts import render,redirect
from .models import Message, Room
from django.contrib.auth.decorators import login_required
from .room_managment import create_room_obj
from django.http import HttpResponse
from django.contrib.auth import get_user_model
import json
# Create your views here.


@login_required
def index(request, room_id):
    room = Room.objects.get(id=room_id)
    latest_messages = room.messages.order_by("timestamp")[:10]
    return render(request, "chat/index.html", {
        "room_id": room_id,
        "latest_messages": latest_messages
        })


@login_required
def room(request, room_id):
    room = Room.objects.get(id=room_id)
    latest_messages = room.messages.order_by("timestamp")[:10]
    return render(request, "chat/room.html", {
        "room_id": room_id,
        "latest_messages": latest_messages
        })


@login_required
def create_room(request):
    if request.method == 'POST':
        User = get_user_model()
        room_creator = request.user
        users = json.loads(request.body.decode('utf-8'))['users']
        users = list(map(lambda user: User.objects.get(username=user), users))
        users.append(room_creator)

        create_room_obj(users, "Group")
        print(users)
    return HttpResponse(status=200)
