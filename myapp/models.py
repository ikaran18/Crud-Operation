from django.db import models


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True,max_length=55)
    roll_id = models.CharField(max_length=7)

from django.contrib.auth.models import AbstractUser
from .manager import *
# Create your models here.

class CustomizeUser(AbstractUser):
    username = None
    email=models.EmailField(unique=True)
    phone_no = models.CharField(max_length=12)
    is_phone_verified = models.BooleanField(default=False)
    
    objects= models.Manager()
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []