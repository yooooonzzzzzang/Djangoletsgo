import imp
from django.contrib import admin
from .models import Music, Artist
# Register your models here.
admin.site.register(Music)
admin.site.register(Artist)
