from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    friends = models.ManyToManyField("self",symmetrical=True)

# Create your models here.
