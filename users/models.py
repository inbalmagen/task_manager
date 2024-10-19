from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    favorite_color = models.CharField(max_length=30,null=True)  
