from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..generic.models import TimestampUserLogModel


class Collection(TimestampUserLogModel):
    expired_on = models.DateTimeField(verbose_name=_("An expiration date"), help_text=_("An expiration date of collection."))
    query = models.CharField(max_length=256)
    comment = models.CharField(max_length=256)
    public = models.BooleanField(default=False)
