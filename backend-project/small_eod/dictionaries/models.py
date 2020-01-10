from django.db import models
from ..generic.models import TimestampUserLogModel


class Dictionary(TimestampUserLogModel):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    min_items = models.IntegerField(default=1)
    max_items = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = "Dictionaries"


class Feature(models.Model):
    dictionary = models.ForeignKey(to=Dictionary, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
