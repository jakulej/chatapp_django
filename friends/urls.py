from django.urls import path
from . import views

urlpatterns = [
        path("find/<str:query>", views.find_friend, name="find-friend"),
]
