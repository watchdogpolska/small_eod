from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..generic.models import TimestampUserLogModel


class Collection(TimestampUserLogModel):
    name = models.CharField(
        max_length=256, verbose_name=_("Name"), help_text=_("Collection's name."),
    )
    expired_on = models.DateTimeField(
        verbose_name=_("An expiration date"),
        help_text=_("An expiration date of collection."),
    )
    queries = models.CharField(
        max_length=256,
        verbose_name=_("Queries"),
        help_text=_("Queries for collection."),
    )
    comments = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=_("Comments"),
        help_text=_("Comments for collection."),
    )
    public = models.BooleanField(
        default=False, verbose_name=_("Public"), help_text=_("Make public.")
    )
