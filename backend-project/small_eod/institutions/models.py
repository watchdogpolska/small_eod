from django.core import validators
from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..administrative_units.models import AdministrativeUnit

from ..generic.models import TimestampUserLogModel
from ..generic.validators import ExactLengthsValidator


class Institution(TimestampUserLogModel):
    name = models.CharField(
        max_length=256, verbose_name=_("Name"), help_text=_("Name of institution")
    )
    administrative_unit = models.ForeignKey(
        to=AdministrativeUnit,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        limit_choices_to=models.Q(category__level=3),
        verbose_name=_("Administrative division"),
        help_text=_("Administrative division."),
    )
    email = models.EmailField(
        blank=True, verbose_name=_("E-mail"), help_text=_("E-mail address.")
    )
    city = models.CharField(
        max_length=100, blank=True, verbose_name=_("City"), help_text=_("Name of city.")
    )
    epuap = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("ePUAP"),
        help_text=_("ePUAP address."),
    )
    street = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Street"),
        help_text=_("Name of street."),
    )
    house_no = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("House number"),
        help_text=_("House number."),
    )
    postal_code = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Postal code"),
        help_text=_("Postal code."),
    )
    flat_no = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Flat number"),
        help_text=_("Flat number."),
    )
    nip = models.CharField(
        max_length=10,
        validators=[ExactLengthsValidator([10]), validators.RegexValidator("^[0-9]*$")],
        blank=True,
        verbose_name=_("NIP"),
        help_text=_("Tax Identification Number."),
    )

    regon = models.CharField(
        max_length=14,
        validators=[
            ExactLengthsValidator([10, 14]),
            validators.RegexValidator("^[0-9]*$"),
        ],
        blank=True,
        verbose_name=_("REGON"),
        help_text=_("Statistical Identification Number."),
    )

    comment = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=_("Comment"),
        help_text=_("Comment for this case."),
    )

    tags = models.ManyToManyField(
        to="tags.Tag", blank=True, verbose_name=_("Tags"), help_text=_("Choose tags.")
    )

    def __str__(self):
        return f"{self.name} ({self.pk})"
