from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# Create your views here.
@login_required
def find_friend(request, query):
    User = get_user_model()
    user = request.user

    result = User.objects.filter(username__icontains=query).exclude(username=user.username)[:5]
    print(result)
    return render(request, "friends/add-friend.html",{"friends_results":result})

def add_friend(request, username):
    if request.method == 'POST':
        User = get_user_model()
        user = request.user
        friend = User.objects.get(username=username)

        user.friends.add(friend)
        user.save()

    return redirect("/chat/index/")
