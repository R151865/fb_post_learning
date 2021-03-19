from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    name = models.CharField(max_length=100)
    profile_pic = models.TextField()
    username = models.CharField(unique=True, max_length=300)