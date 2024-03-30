from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
     photo = models.ImageField(upload_to='profile_pic', default='default.jpg')
     name=models.CharField(max_length=30)
     email=models.CharField(max_length=40)
     password=models.CharField(max_length=20)
     about=models.CharField(max_length=300)