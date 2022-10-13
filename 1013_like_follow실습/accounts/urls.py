from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
    # 프로필 페이지 기능 구현
    path('<username>/', views.profile, name='profile'),
    # 팔로우를 하기 위한 기능 구현
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]
