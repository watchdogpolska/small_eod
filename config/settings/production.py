from .base import *  # noqa

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")

INSTALLED_APPS = INSTALLED_APPS + ["raven.contrib.django.raven_compat"]
FILE_UPLOAD_PERMISSIONS = 0o644
