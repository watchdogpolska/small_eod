from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission


@receiver(pre_save, sender=User)
def set_group(sender, **kwargs):
    user = kwargs["instance"]
    if user.is_staff == 0:
        user.is_staff = 1
    else:
        pass


@receiver(post_save, sender=User)
def set_permissions(sender, **kwargs):
    u, created = kwargs["instance"], kwargs["created"]
    if created:

        permission = Permission.objects.get(content_type=1, codename='view_Case')
        permission1 = Permission.objects.get(content_type=1, codename='view_letter')
        u.user_permissions.add(permission)
        u.user_permissions.add(permission1)
    else:
        pass
