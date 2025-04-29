from django.shortcuts import render,redirect
from .models import Message, Room
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    return render(request, "chat/index.html")

@login_required
def room(request, room_id):
    room = Room.objects.get(id=room_id)
    latest_messages = room.messages.order_by("timestamp")[:10]
    return render(request, "chat/room.html", {"room_id": room_id, "latest_messages": latest_messages})
