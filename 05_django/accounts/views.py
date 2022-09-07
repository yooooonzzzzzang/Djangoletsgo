from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm
# Create your views here.
def login(request):
    if request.method =='POST':
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():#로그인 request, 유저정보
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context ={
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    # 로그아웃
    auth_logout(request)
    return redirect('articles:index')

#create
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 회원가입 후 로그인
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context ={
        'form' : form,
    }
    return render(request,'accounts/signup.html', context)

def delete(request):
    # 유저데이터.delete() 
    request.user.delete()
    auth_logout(request)  # 탈퇴 -> 로그아웃 순서 로그아웃 먼저 하면 request요청 사라짐
    return redirect('articles:index')

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context ={
        'form' : form,
    }
    return render(request, 'accounts/update.html', context)
