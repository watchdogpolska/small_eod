from django.apps import AppConfig
from django.conf import settings


class EventsConfig(AppConfig):
    name = 'events'

class EventsSettings:
    FROM_EMAIL = getattr(settings, 'EVENTS_FROM_EMAIL', 'example@localhost')
