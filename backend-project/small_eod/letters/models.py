from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..cases.models import Case
from ..channels.models import Channel
from ..generic.models import TimestampUserLogModel
from ..institutions.models import Institution
from django.utils.timezone import datetime


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
        verbose_name=_("Date"),
        help_text=_("Date of sending or receiving."),
        default=datetime.now,
    )
    final = models.BooleanField(
        verbose_name=_("Final version"),
        default=True,
        help_text=_(
            "Indicates whether the document has "
            + "final content or is, for example, a draft"
        ),
    )
    name = models.CharField(
        max_length=256,
        verbose_name=_("Description"),
        help_text=_("Description of the letter."),
    )
    ordering = models.IntegerField(
        default=0, verbose_name=_("Ordering"), help_text=_("Order of letter.")
    )
    comments = models.CharField(
        max_length=256,
        verbose_name=_("Comments"),
        help_text=_("Comments for letter."),
        blank=True,
    )
    excerpts = models.CharField(
        max_length=256,
        verbose_name=_("Excerpts"),
        help_text=_("Excerpts of letter."),
        blank=True,
    )
    identifier = models.CharField(
        max_length=256,
        verbose_name=_("Identifier"),
        help_text=_("Identifier of letter."),
        blank=True,
    )
    cases = models.ForeignKey(
        to=Case,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Case"),
        null=True,
        blank=True,
    )
    channels = models.ForeignKey(
        to=Channel,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Channels"),
        blank=True,
        null=True,
    )
    institutions = models.ForeignKey(
        to=Institution,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Institutions"),
        blank=True,
        null=True,
    )
    descriptions = models.ForeignKey(
        to=Description,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Descriptions of letter."),
        null=True,
        blank=True,
    )
