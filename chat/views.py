from django.shortcuts import render, redirect
from .models import Message, Room
from django.db.models import Max, Field
from django.contrib.auth.decorators import login_required
from .room_managment import create_room_obj
from django.http import HttpResponse
from django.contrib.auth import get_user_model
import json
# Create your views here.


@login_required
def index(request):
    latest_room_id = sort_rooms_latest_message(request.user)[0].id
    room_url = "/chat/"+str(latest_room_id)
    return redirect(room_url)


@login_required
def room(request, room_id):
    room = Room.objects.get(id=room_id)
    room.name = set_room_name(room, request.user)
    latest_messages = room.messages.order_by("timestamp")[:10]
    return render(request, "chat/index.html", {
        "current_room": room,
        "latest_messages": latest_messages,
        "sorted_rooms": sort_rooms_latest_message(request.user)
        })


@login_required
def create_room(request):
    if request.method == 'POST':
        User = get_user_model()
        room_creator = request.user

        data = json.loads(request.body.decode('utf-8'))
        users = data['users']
        group_name = data['group_name']
        users = list(map(lambda user: User.objects.get(username=user), users))
        users.append(room_creator)

        create_room_obj(users, group_name)
        print(users)
    return HttpResponse(status=200)


def sort_rooms_latest_message(user):
    rooms = user.rooms.all()

    for room in rooms:
        last_message = room.messages.order_by('-timestamp').first()
        if last_message:
            last_message.content = cut_text(last_message.content, 10)
        room.last_message = last_message
        room.name = set_room_name(room, user)
    return rooms


def cut_text(text, max_lenght):
    shorted = text[:max_lenght]
    if len(text) > max_lenght:
        shorted = shorted + "..."
    return shorted


def set_room_name(room, current_user):
    name = room.name
    if room.name is None:
        usernames = room.users.all().exclude(id=current_user.id).values_list("username", flat=True)
        name = ", ".join(usernames)
    return name
