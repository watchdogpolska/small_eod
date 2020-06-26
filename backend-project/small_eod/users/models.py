from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import Value as V
from django.db.models.functions import Concat


class CustomUserManager(UserManager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .annotate(official_name=Concat("first_name", V(" "), "last_name"))
        )


class User(AbstractUser):
    objects = CustomUserManager()
