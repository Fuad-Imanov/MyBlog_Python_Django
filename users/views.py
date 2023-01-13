from django.contrib import messages
from django.contrib.auth import login,logout

from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm


# Create your views here.

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages(request, 'Qeydiyyatda sehv var')
    else:
        form = RegisterForm(request.POST)
    return render(request, 'users/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')


    else:
        form = LoginForm(request.POST)
    return render(request, 'users/login.html', {'form': form})