from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.sessions.models import Session


class User(AbstractUser):
    pass


class Description(models.Model):
    sessions = models.ForeignKey(to=Session, on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    userAgent = models.CharField(max_length=512)
