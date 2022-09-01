from operator import mod
from pyexpat import model
from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    creaeted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)