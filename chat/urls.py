from django.urls import path
from chat import views as chat_views
from . import views

urlpatterns = [
    path('', chat_views.chatPage, name='chat-page')
]