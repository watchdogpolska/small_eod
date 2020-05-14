from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..cases.models import Case
from ..generic.models import TimestampUserLogModel


class Note(TimestampUserLogModel):
    comment = models.CharField(max_length=256, verbose_name=_("Comment"))
    case = models.ForeignKey(
        to=Case,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Case"),
        help_text=_("Related case."),
    )
