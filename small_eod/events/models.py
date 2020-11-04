from django.db import models
from django.utils.translation import ugettext_lazy as _
from ..cases.models import Case
from ..authkey.models import TimestampUserLogModel


class Event(TimestampUserLogModel):
    date = models.DateTimeField(verbose_name=_("Date"), help_text=_("Date of event."))
    name = models.CharField(
        max_length=256, verbose_name=_("Name"), help_text=_("Name of event.")
    )
    comment = models.CharField(
        max_length=256, verbose_name=_("Comment"), help_text=_("Comment text.")
    )
    case = models.ForeignKey(
        to=Case,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Case"),
        help_text=_("Case for this event."),
    )
