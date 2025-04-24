from django.shortcuts import render
from django.contrib.auth import get_user_model

# Create your views here.
def find_friend(request, query):
    User = get_user_model()
    result = User.objects.filter(username__icontains=query)[:5]
    return render(request, "friends/add-friend.html",{"friend_result":result})
