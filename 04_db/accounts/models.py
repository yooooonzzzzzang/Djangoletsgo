from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    pass

# 빌트인 자체가 username 을 출력하게 되어있어서 user 만 출력해도 
# username 이 나온다.
    # def __str__(self) -> str:
    #     return self.username
