from django.db import models

from ..generic.models import TimestampUserLogModel


class Collection(TimestampUserLogModel):

    comment = models.CharField(max_length=256)
    public = models.BooleanField(default=False)
    expired_on = models.DateTimeField()
    query = models.CharField(max_length=256)
