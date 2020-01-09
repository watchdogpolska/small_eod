from django.db import models
from django.core.validators import RegexValidator
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from ..generic.models import TimestampUserLogModel


class TagNamespace(TimestampUserLogModel):
    description = models.CharField(max_length=256)
    color = models.CharField(
        max_length=6,
        default='000000',
        validators=[
            RegexValidator(
                regex=r'^(?:[a-f0-9]{6})|(?:[A-F0-9]{6})$',
                message="Field must be hexadecimal RGB color",
                code="Non_RGB_hex"
            )
        ]
    )


class Tag(models.Model):
    name = models.CharField(max_length=256)
