from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..generic.models import TimestampUserLogModel


class Dictionary(TimestampUserLogModel):
    name = models.CharField(
        max_length=100, verbose_name=_("Name"), help_text=_("Name of dictionary.")
    )
    min_items = models.IntegerField(
        default=1, verbose_name=_("Min. items"), help_text=_("Minimum number of items.")
    )
    max_items = models.IntegerField(
        default=1, verbose_name=_("Max. items"), help_text=_("Maximum number of items.")
    )
    active = models.BooleanField(
        default=False, verbose_name=_("Active"), help_text=_("Make active.")
    )

    class Meta:
        verbose_name_plural = "Dictionaries"


class Feature(models.Model):
    name = models.CharField(
        max_length=100, verbose_name=_("Name"), help_text=_("Name of feature.")
    )
    dictionary = models.ForeignKey(
        to=Dictionary,
        on_delete=models.CASCADE,
        verbose_name=_("Dictionary"),
        help_text=_("Related dictionary."),
    )
