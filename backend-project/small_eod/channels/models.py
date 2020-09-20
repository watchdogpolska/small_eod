from django.db import models
from ..generic.models import TimestampUserLogModel
from django.utils.translation import ugettext_lazy as _


class Channel(TimestampUserLogModel):
    name = models.CharField(
        max_length=25,
        verbose_name=_("Name"),
        help_text=_("Channel's name."),
    )
    city = models.BooleanField(
        default=False,
        verbose_name=_("City"),
        help_text=_(
            "Name of city in institution address is mandatory for this channel."
        ),
    )
    email = models.BooleanField(
        default=False,
        verbose_name=_("E-mail"),
        help_text=_("Institution e-mail address is mandatory for this channel."),
    )
    epuap = models.BooleanField(
        default=False,
        verbose_name=_("ePUAP"),
        help_text=_("Institution ePUAP address is mandatory for this channel."),
    )
    street = models.BooleanField(
        default=False,
        verbose_name=_("Street"),
        help_text=_(
            "Name of street in institution address is mandatory for this channel."
        ),
    )
    flat_no = models.BooleanField(
        default=False,
        verbose_name=_("Flat number"),
        help_text=_(
            "Flat number in institution address is mandatory for this channel."
        ),
    )
    house_no = models.BooleanField(
        default=False,
        verbose_name=_("House number"),
        help_text=_(
            "House number in institution address is mandatory for this channel."
        ),
    )
    postal_code = models.BooleanField(
        default=False,
        verbose_name=_("Postal code"),
        help_text=_(
            "Postal code in institution address is mandatory for this channel."
        ),
    )
    voivodeship = models.BooleanField(
        default=False,
        verbose_name=_("Voivodeship"),
        help_text=_(
            "Voivodeship in institution address is mandatory for this channel."
        ),
    )
