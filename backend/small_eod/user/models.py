from django.contrib.sessions.models import Session

from django.db import models
from django.contrib.auth.models import AbstractUser
from guardian.mixins import GuardianUserMixin


class User(GuardianUserMixin, AbstractUser):
    def __str__(self):
        return self.username


class Description(models.Model):
    text = models.CharField(max_length=256)
    userAgent = models.CharField(max_length=512)
