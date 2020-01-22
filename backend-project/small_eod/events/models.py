from django.db import models
from ..generic.models import TimestampUserLogModel
from ..cases.models import Case


class Event(TimestampUserLogModel):
    data = models.DateTimeField()
    name = models.CharField(max_length=256)
    comment = models.CharField(max_length=256)
    case = models.ForeignKey(to=Case, on_delete=models.DO_NOTHING)
