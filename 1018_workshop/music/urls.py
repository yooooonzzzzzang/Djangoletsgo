from django.urls import path
from . import views

urlpatterns = [
    path('artist/', views.artist_list),
    path('artist/<int:artist_pk>/', views.artist_detail),
    path('artist/<int:artist_pk>/music/', views.music_create),
    path('music/', views.music_list),
    path('music/<int:music_pk>/', views.music_detail),

]
