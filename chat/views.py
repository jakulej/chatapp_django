from django.shortcuts import render,redirect
from .models import Message, Room
from django.contrib.auth.decorators import login_required
from .room_managment import create_room
from django.http import HttpResponse
# Create your views here.
@login_required
def index(request):
    return render(request, "chat/index.html")

@login_required
def room(request, room_id):
    room = Room.objects.get(id=room_id)
    latest_messages = room.messages.order_by("timestamp")[:10]
    return render(request, "chat/room.html", {"room_id": room_id, "latest_messages": latest_messages})

@login_required
def create_room(request):
    if request.method == 'POST':
        user = request.user
        print(request.body.users)
    return HttpResponse(status=200)
    
