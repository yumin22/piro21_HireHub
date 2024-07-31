from django.db import models
from django.contrib.auth.models import AbstractUser

class Interviewer(AbstractUser):
    username = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=255, unique=True)
    is_approved = models.BooleanField(default=False) # 승인을 해야 로그이 가능하게 하기 위해서 둠!

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']