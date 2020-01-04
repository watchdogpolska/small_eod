from django.db import models
from ..generic.models import TimestampUserLogModel


class Channel(TimestampUserLogModel):

    class Name(models.TextChoices):
        FED = 'FED', 'fedrowanie'
        FAX = 'FAX', 'faks'
        CUS = 'CUS', 'od klienta'
        MEC = 'MEC', 'mecenas zewnętrzny'
        PER = 'PER', 'dostarczenie osobiste'
        EMAIL = 'EMAIL', 'email'
        POST = 'POST', 'poczta tradycyjna'
        EPUAP = 'EPUAP', 'epuap'

    name = models.CharField(
        choices=Name.choices,
        max_length=5
    )
    city = models.BooleanField(default=False)
    voivodeship = models.BooleanField(default=False)
    flat_no = models.BooleanField(default=False)
    street = models.BooleanField(default=False)
    postal_code = models.BooleanField(default=False)
    house_no = models.BooleanField(default=False)
    email = models.BooleanField(default=False)
    epuap = models.BooleanField(default=False)
