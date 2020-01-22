from django.db import models

from ..cases.models import Case
from ..channels.models import Channel
from ..generic.models import TimestampUserLogModel
from ..institutions.models import Institution, AddressData


class Letter(TimestampUserLogModel):
    class Direction(models.TextChoices):
        IN = "IN", "Received"
        OUT = "OUT", "Sent"

    direction = models.TextField(
        choices=Direction.choices, default=Direction.IN, max_length=3
    )

    date = models.DateTimeField()
    final = models.BooleanField()

    name = models.CharField(max_length=256)
    ordering = models.IntegerField(default=0)
    comment = models.CharField(max_length=256)
    excerpt = models.CharField(max_length=256)
    identifier = models.CharField(max_length=256)

    case = models.ForeignKey(to=Case, on_delete=models.DO_NOTHING)
    channel = models.ForeignKey(to=Channel, on_delete=models.DO_NOTHING)
    address = models.ForeignKey(to=AddressData, on_delete=models.DO_NOTHING)
    institution = models.ForeignKey(to=Institution, on_delete=models.DO_NOTHING)


class Description(models.Model):
    name = models.CharField(max_length=256)
