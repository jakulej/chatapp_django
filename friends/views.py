from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from chat.room_managment import create_room_obj
# Create your views here.
@login_required
def find_friend(request, query):
    User = get_user_model()
    user = request.user

    result = User.objects.filter(username__icontains=query).exclude(username=user.username)[:5]
    print(result)
    return render(request, "friends/add-friend.html",{"friends_results":result})

@login_required
def add_friend(request, username):
    if request.method == 'POST':
        User = get_user_model()
        user = request.user
        friend = User.objects.get(username=username)

        user.friends.add(friend)
        user.save()
        create_room_obj([user, friend],"temp")

    return redirect("/chat/index/")
