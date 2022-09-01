from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.read, name = 'read'),
    path('new/', views.new, name = 'new'),
    path('create/', views.create, name = 'create'),
    path('<int:pk>', views.detail, name = 'detail'),
    
]
