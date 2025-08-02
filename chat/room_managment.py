from . import models
from .models import Room


def create_room(users, room_name):
    room = Room(name = room_name)
    room.save()
    room.users.set(users)
    pass


