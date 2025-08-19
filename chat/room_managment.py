from . import models
from .models import Room


def create_room_obj(users, room_name = None):
    room = Room()
    if room_name is not None:
        room.name = room_name
    room.save()
    room.users.set(users)
    pass

def get_latest_room(user):
    pass
