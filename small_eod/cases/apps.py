from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CasesConfig(AppConfig):
    name = 'small_eod.cases'
    verbose_name = _("Cases")