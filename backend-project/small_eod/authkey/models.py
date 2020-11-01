import binascii
import os

from django.utils.timezone import now, timedelta
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from ..generic.models import TimestampUserLogModel

update_interval = timedelta(minutes=15)


def generate_token():
    return binascii.hexlify(os.urandom(20)).decode()


class Scope(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Name"))

    def __str__(self) -> str:
        return self.name


class Key(TimestampUserLogModel):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    token = models.CharField(
        verbose_name=_("Token"),
        max_length=40,
        unique=True,
        default=generate_token,
    )
    scopes = models.ManyToManyField(verbose_name=_("Scopes"), to=Scope)
    used_on = models.DateTimeField(default=now, verbose_name=_("Date of last used"))

    def has_scopes(self, scopes):
        available = {x.name for x in self.scopes.all()}
        missing = set(scopes) - available
        return len(missing) == 0

    def update_used_on(self, save=True):
        # only update if time exceeds the threshold
        # allows reduce number of queries in case of a series of requests
        if now() - self.used_on < update_interval:
            return False
        self.used_on = now()
        if save:
            self.save()
        return True
