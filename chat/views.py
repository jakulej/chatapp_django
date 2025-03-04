from django.shortcuts import render,redirect

# Create your views here.

def chatPage(request):
    return render(request, "chat/chatPage.html")
