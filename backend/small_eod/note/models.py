from django.db import models

from case.models import Case
from generic.models import TimestampUserLogModel


class Note(TimestampUserLogModel):
    case = models.ForeignKey(to=Case, on_delete=models.DO_NOTHING)
    comment = models.CharField(max_length=256)

