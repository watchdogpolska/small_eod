from django.db import models

from ..cases.models import Case
from ..generic.models import TimestampUserLogModel


class Note(TimestampUserLogModel):
    comment = models.CharField(max_length=256)
    case = models.ForeignKey(to=Case, on_delete=models.DO_NOTHING)
