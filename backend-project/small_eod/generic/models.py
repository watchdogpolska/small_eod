# Create your models here.
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class TimestampUserLogModel(models.Model):

    modified_on = models.DateTimeField(
        auto_now=True, verbose_name=_("Date of the modification")
    )
    created_on = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Date of creation")
    )

    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name="%(class)s_created_by",
        null=True,
        blank=True,
        verbose_name=_("Created by"),
    )
    modified_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name="%(class)s_modified_by",
        null=True,
        blank=True,
        verbose_name=_("Modified by"),
    )

    class Meta:
        abstract = True
