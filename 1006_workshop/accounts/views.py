from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CustomUserCreationForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)

def login(reqeust):
    if reqeust.method == 'POST':
        form = AuthenticationForm(reqeust, reqeust.POST)
        if form.is_valid():
            auth_login(reqeust, form.get_user())
            return redirect('todos:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(reqeust, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:login')
