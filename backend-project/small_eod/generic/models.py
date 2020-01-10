from django.db import models

# Create your models here.
from django.conf import settings


class TimestampUserLogModel(models.Model):

    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name="%(class)s_created_by",
        null=True,
        blank=True,
    )
    modified_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name="%(class)s_modified_by",
        null=True,
        blank=True,
    )

    modified_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
