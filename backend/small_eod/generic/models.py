from django.db import models

# Create your models here.
from django.conf import settings


class TimestampUserLogModel(models.Model):

    createdBy = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='%(class)s_createdBy',
        null=True,
        blank=True
    )
    modifiedBy = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='%(class)s_modifiedBy',
        null=True,
        blank=True
    )

    modifiedOn = models.DateTimeField(auto_now=True)
    createdOn = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
