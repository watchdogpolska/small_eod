# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from django.db.models import Q


@receiver(pre_save, sender=User)
def set_group(sender, **kwargs):
    user = kwargs["instance"]
    if user.is_staff == 0:
        user.is_staff = 1


@receiver(post_save, sender=User)
def set_permissions(sender, **kwargs):
    u, created = kwargs["instance"], kwargs["created"]

    if created and u.email.endswith('@siecobywatelska.pl'):
        permission = Permission.objects.filter(Q(content_type__app_label='Cases', content_type__model='Case',
                                                 codename='view_case') | Q(content_type__app_label='Cases',
                                               content_type__model='Letter', codename='view_letter'))
        u.user_permissions.set(permission)
