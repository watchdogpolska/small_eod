from .base import *  # noqa

DEBUG = True

TEMPLATES[0]["OPTIONS"]["debug"] = True

INSTALLED_APPS += ["debug_toolbar", "django_extensions"]

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware", ]

INTERNAL_IPS = [
    "127.0.0.1",
]

ALLOWED_HOSTS = ["*"]
DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": lambda request: True}

SECRET_KEY = "development"
