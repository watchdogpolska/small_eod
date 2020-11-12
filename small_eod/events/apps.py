from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EventConfig(AppConfig):
    name = "small_eod.events"
    verbose_name = _("Events")
