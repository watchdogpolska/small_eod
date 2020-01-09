# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth.models import Permission
# from django.db.models import Q

# @receiver(post_save, sender=User)
# def set_permissions(instance, created, **kwargs):
#     if created and instance.email.endswith("@siecobywatelska.pl"):
#         instance.is_staff = 1
#         permission = Permission.objects.filter(
#             Q(
#                 content_type__app_label="Cases",
#                 content_type__model="Case",
#                 codename="view_case",
#             )
#             | Q(
#                 content_type__app_label="Cases",
#                 content_type__model="Letter",
#                 codename="view_letter",
#             )
#         )
#         instance.user_permissions.set(permission)
#         instance.save()
