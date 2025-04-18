from django.shortcuts import render, redirect
from django.contrib.auth.forms import BaseUserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    return render(request, "accounts/login.html")

def register(request):
    if request.method == 'POST':
        form =  BaseUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/accounts/login")
    else:
        form = BaseUserCreationForm()
    return render(request, "registration/register.html",{"form":form})
