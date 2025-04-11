from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.sender}: {self.content}'

class Room(models.Model):
    users = models.ManyToManyField(User)   
    messages = models.ManyToManyField(Message)
