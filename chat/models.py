from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Room(models.Model):
    users = models.ManyToManyField(User, related_name='rooms')   
    name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name}'


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.sender}: {self.content}'
