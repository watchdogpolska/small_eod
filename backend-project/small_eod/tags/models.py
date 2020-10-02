from django.db import models
from django.core.validators import RegexValidator

from ..generic.models import TimestampUserLogModel
from django.utils.translation import ugettext_lazy as _


class TagNamespace(TimestampUserLogModel):
    description = models.CharField(max_length=256, verbose_name=_("Description"))

    prefix = models.CharField(
        max_length=254,
        verbose_name=_("Prefix"),
        help_text=_("This namespace will match each tag starting with `prefix`."),
    )

    color = models.CharField(
        max_length=6,
        verbose_name=_("Color"),
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
    name = models.CharField(max_length=256, verbose_name=_("Tag"), unique=True)

    def __str__(self):
        return self.name
