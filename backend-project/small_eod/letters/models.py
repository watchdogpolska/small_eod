from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..cases.models import Case
from ..channels.models import Channel
from ..generic.models import TimestampUserLogModel
from ..institutions.models import Institution, AddressData


class Description(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name=_("Description"),
        help_text=_("Description of letter."),
    )


class Letter(TimestampUserLogModel):
    class Direction(models.TextChoices):
        IN = "IN", "Received"
        OUT = "OUT", "Sent"

    direction = models.TextField(
        choices=Direction.choices,
        default=Direction.IN,
        max_length=3,
        verbose_name=_("Direction"),
        help_text=_("Direction for letter."),
    )

    date = models.DateTimeField(
        verbose_name=_("Date"), help_text=_("Date of sending or receiving.")
    )
    final = models.BooleanField()

    name = models.CharField(
        max_length=256,
        verbose_name=_("Description"),
        help_text=_("Description of the letter."),
    )
    ordering = models.IntegerField(
        default=0, verbose_name=_("Ordering"), help_text=_("Order of letter.")
    )
    comment = models.CharField(
        max_length=256, verbose_name=_("Comment"), help_text=_("Comment for letter.")
    )
    excerpt = models.CharField(
        max_length=256, verbose_name=_("Excerpt"), help_text=_("Excerpt of letter.")
    )
    identifier = models.CharField(
        max_length=256,
        verbose_name=_("Identifier"),
        help_text=_("Identifier of letter."),
    )

    case = models.ForeignKey(
        to=Case, on_delete=models.DO_NOTHING, verbose_name=_("Case"),
    )
    channel = models.ForeignKey(
        to=Channel, on_delete=models.DO_NOTHING, verbose_name=_("Channel"),
    )
    address = models.ForeignKey(
        to=AddressData, on_delete=models.DO_NOTHING, verbose_name=_("Address"),
    )
    institution = models.ForeignKey(
        to=Institution, on_delete=models.DO_NOTHING, verbose_name=_("Institution"),
    )
    description = models.ForeignKey(
        to=Description,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Description of letter."),
        null=True,
        blank=True,
    )
