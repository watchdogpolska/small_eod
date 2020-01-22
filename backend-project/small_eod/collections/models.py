from django.db import models

from ..generic.models import TimestampUserLogModel


class Collection(TimestampUserLogModel):
    expired_on = models.DateTimeField()
    query = models.CharField(max_length=256)
    comment = models.CharField(max_length=256)
    public = models.BooleanField(default=False)
