from django.db import models
from generic.models import TimestampUserLogModel
from channel.models import Channel
from institution.models import Institution, AddressData
from case.models import Case


class Letter(TimestampUserLogModel):

    class Direction(models.TextChoices):
        IN = 'IN', 'Received'
        OUT = 'OUT', 'Sent'

    direction = models.TextField(choices=Direction.choices, default=Direction.IN, max_length=3)
    name = models.CharField(max_length=256)
    channel = models.ForeignKey(to=Channel, on_delete=models.DO_NOTHING)
    final = models.BooleanField()
    date = models.DateTimeField()
    identifier = models.CharField(max_length=256)
    institution = models.ForeignKey(to=Institution, on_delete=models.DO_NOTHING)
    address = models.ForeignKey(to=AddressData, on_delete=models.DO_NOTHING)
    case = models.ForeignKey(to=Case, on_delete=models.DO_NOTHING)
    ordering = models.IntegerField(default=0)
    comment = models.CharField(max_length=256)
    excerpt = models.CharField(max_length=256)


