from django.db import models
from generic.models import TimestampUserLogModel


class Required(models.Model):
    city = models.BooleanField()
    voivodeship = models.BooleanField()
    flat_no = models.BooleanField()
    street = models.BooleanField()
    postal_code = models.BooleanField()
    house_no = models.BooleanField()
    email = models.BooleanField()
    epuap = models.BooleanField()


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
        default=Name.EMAIL,
        max_length=5
    )
    required = models.OneToOneField(to=Required, on_delete=models.CASCADE)

