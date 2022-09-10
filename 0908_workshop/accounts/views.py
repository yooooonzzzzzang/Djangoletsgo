from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login
# Create your views here.
def index(request):
    User = get_user_model()
    members = User.objects.all()
    context = {
        'members' : members,
    }
    return render(request, 'accounts/index.html', context)

# 회원가입 
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)

# 로그인
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    context ={
        'form' : form
    }
    return render(request, 'accounts/login.html', context)

# 비밀번호 변경
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/change_password.html', context)