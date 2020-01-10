from .base import *  # noqa

DEBUG = True

TEMPLATES[0]["OPTIONS"]["debug"] = True

INSTALLED_APPS += [
    "debug_toolbar",
    "django_extensions"
]

MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware", ] + MIDDLEWARE

INTERNAL_IPS = [
    "127.0.0.1",
]

ALLOWED_HOSTS = ["*"]
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda r: r.environ.get('SERVER_NAME', None) != 'testserver' and (r.META.get('REMOTE_ADDR', None) in INTERNAL_IPS)
}

SECRET_KEY = "development"

REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES'] = []
