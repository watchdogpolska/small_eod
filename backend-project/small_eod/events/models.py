from django.db import models
from django.utils.translation import ugettext_lazy as _
from ..generic.models import TimestampUserLogModel
from ..cases.models import Case


class Event(TimestampUserLogModel):
    date = models.DateTimeField(verbose_name=_("Date"), help_text=_("Date of event."))
    name = models.CharField(
        max_length=256, verbose_name=_("Name"), help_text=_("Name of event.")
    )
    comments = models.CharField(
        max_length=256, verbose_name=_("Comments"), help_text=_("Comments text.")
    )
    cases = models.ForeignKey(
        to=Case,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Cases"),
        help_text=_("Cases for this event."),
    )
