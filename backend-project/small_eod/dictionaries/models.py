from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..generic.models import TimestampUserLogModel


class Dictionary(TimestampUserLogModel):
    name = models.CharField(max_length=100, verbose_name=_("Name"), help_text=_("Name of dictionary."))
    min_items = models.IntegerField(default=1)
    max_items = models.IntegerField(default=1)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Dictionaries"


class Feature(models.Model):
    name = models.CharField(max_length=100)
    dictionary = models.ForeignKey(to=Dictionary, on_delete=models.CASCADE)
