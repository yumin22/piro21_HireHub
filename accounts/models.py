from django.db import models
from django.contrib.auth.models import AbstractUser

class Interviewer(AbstractUser):
    company_name = models.CharField(max_length=200)
    is_approved = models.BooleanField(default=False) # 승인을 해야 로그이 가능하게 하기 위해서 둠!
    
