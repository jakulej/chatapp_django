from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages

# Create your views here.
def login(request):
    return render(request, "accounts/login.html")

def register(request):
    if request.method == 'POST':
        form =  RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Created Account, Now you can login")
            return redirect("/accounts/login")
    else:
        form = RegisterForm()
    return render(request, "registration/register.html",{"form":form})
