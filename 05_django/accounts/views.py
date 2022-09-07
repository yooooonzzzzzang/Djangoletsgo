from importlib.metadata import requires
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
# Create your views here.
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')


    if request.method =='POST':
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():#로그인 request, 유저정보
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:ind ex')
    else:
        form = AuthenticationForm()
    context ={
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)

@require_POST
def logout(request):
    # 로그아웃
    auth_logout(request)
    return redirect('articles:index')

#create
@require_http_methods(['GET', 'POST'])
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
@login_required
@require_http_methods(['GET','POST'])
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
@login_required
@require_http_methods(['GET','POST'])
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:                       # 필수인자 필요
        form = PasswordChangeForm(request.user)
       
    context = {
        'form' : form,
    }
    return render(request, 'accounts/change_password.html', context)
