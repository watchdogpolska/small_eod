from django.db import models
from django.core.validators import RegexValidator

from ..generic.models import TimestampUserLogModel
from django.utils.translation import ugettext_lazy as _


class TagNamespace(TimestampUserLogModel):
    prefix = models.CharField(
        max_length=254,
        help_text=_("This namespace will match each tag starting with `prefix`."),
    )
    description = models.CharField(max_length=256)
    color = models.CharField(
        max_length=6,
        default="000000",
        validators=[
            RegexValidator(
                regex=r"^(?:[a-f0-9]{6})|(?:[A-F0-9]{6})$",
                message="Field must be hexadecimal RGB color",
                code="Non_RGB_hex",
            )
        ],
    )


class Tag(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
