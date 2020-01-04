from django.db import models
from generic.models import TimestampUserLogModel
from case.models import Case


class Event(TimestampUserLogModel):
    case = models.ForeignKey(to=Case, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=256)
    data = models.DateTimeField()
    comment = models.CharField(max_length=256)
