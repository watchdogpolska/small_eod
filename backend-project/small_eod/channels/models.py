from django.db import models
from ..generic.models import TimestampUserLogModel
from django.utils.translation import ugettext_lazy as _


class Channel(TimestampUserLogModel):
    name = models.CharField(max_length=25,
                            verbose_name=_("Name"),
                            help_text=_("Channel's name. Name cannot be longer than 25 characters."))
    city = models.BooleanField(default=False,
                               verbose_name=_("City"),
                               help_text=_("Name of city in institution address is mandatory for this channel."))
    email = models.BooleanField(default=False,
                                verbose_name=_("E-mail"),
                                help_text=_("Institution e-mail address is mandatory for this channel."))
    epuap = models.BooleanField(default=False)
    street = models.BooleanField(default=False)
    flat_no = models.BooleanField(default=False)
    house_no = models.BooleanField(default=False)
    postal_code = models.BooleanField(default=False)
    voivodeship = models.BooleanField(default=False)
