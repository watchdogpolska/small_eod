from django.db import models
from ..generic.models import TimestampUserLogModel


class Channel(TimestampUserLogModel):
    name = models.CharField(max_length=25)
    city = models.BooleanField(default=False)
    voivodeship = models.BooleanField(default=False)
    flat_no = models.BooleanField(default=False)
    street = models.BooleanField(default=False)
    postal_code = models.BooleanField(default=False)
    house_no = models.BooleanField(default=False)
    email = models.BooleanField(default=False)
    epuap = models.BooleanField(default=False)
