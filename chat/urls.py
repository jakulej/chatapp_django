from django.urls import path
from chat import views as chat_views
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:room_id>/", views.room, name="room"),
]
