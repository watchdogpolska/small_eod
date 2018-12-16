from .base import *  # noqa

DEBUG = True

TEMPLATES[0]['OPTIONS']['debug'] = True

INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar',
    'django_extensions'
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
] + MIDDLEWARE

INTERNAL_IPS = ['127.0.0.1', ]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ALLOWED_HOSTS = ['*']

SECRET_KEY='development'