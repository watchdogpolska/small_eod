from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..cases.models import Case
from ..channels.models import Channel
from ..generic.models import TimestampUserLogModel
from ..institutions.models import Institution
from django.utils import timezone


class DocumentType(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name=_("Document type"),
        help_text=_("Type of letter"),
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
        default=timezone.now,
    )
    final = models.BooleanField(
        verbose_name=_("Final version"),
        default=True,
        help_text=_(
            "Indicates whether the document has "
            + "final content or is, for example, a draft"
        ),
    )
    ordering = models.IntegerField(
        default=0, verbose_name=_("Ordering"), help_text=_("Order of letter.")
    )
    comment = models.CharField(
        max_length=256,
        verbose_name=_("Comment"),
        help_text=_("Comment for letter."),
        blank=True,
    )
    excerpt = models.CharField(
        max_length=256,
        verbose_name=_("Excerpt"),
        help_text=_("Excerpt of letter."),
        blank=True,
    )
    reference_number = models.CharField(
        max_length=256,
        verbose_name=_("Reference number"),
        help_text=_("Reference number of letter."),
        blank=True,
    )
    case = models.ForeignKey(
        to=Case,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Case"),
        null=True,
        blank=True,
    )
    channel = models.ForeignKey(
        to=Channel,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Channel"),
        blank=True,
        null=True,
    )
    institution = models.ForeignKey(
        to=Institution,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Institution"),
        blank=True,
        null=True,
    )
    document_type = models.ForeignKey(
        to=DocumentType,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Document type of letter."),
        null=True,
        blank=True,
    )
