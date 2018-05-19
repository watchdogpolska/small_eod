from .base import *  # noqa

INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar',
    'django_extensions'
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
] + MIDDLEWARE

INTERNAL_IPS = ['127.0.0.1', ]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'