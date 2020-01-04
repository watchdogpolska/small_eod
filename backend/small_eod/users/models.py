from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Description(models.Model):
    text = models.CharField(max_length=256)
    userAgent = models.CharField(max_length=512)
