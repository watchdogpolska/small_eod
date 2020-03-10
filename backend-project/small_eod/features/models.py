from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..generic.models import TimestampUserLogModel


class Feature(TimestampUserLogModel):
    name = models.CharField(
        max_length=100, verbose_name=_("Name"), help_text=_("Name of feature.")
    )
    min_options = models.IntegerField(
        default=1,
        verbose_name=_("Min. options"),
        help_text=_("Minimum number of selected option (if any)."),
    )
    max_options = models.IntegerField(
        default=1,
        verbose_name=_("Max. options"),
        help_text=_("Maximum number of selected option."),
    )

    class Meta:
        verbose_name_plural = "Features"


class FeatureOption(models.Model):
    name = models.CharField(
        max_length=100, verbose_name=_("Name"), help_text=_("Name of option.")
    )
    feature = models.ForeignKey(
        to=Feature,
        on_delete=models.CASCADE,
        related_name='featureoptions',
        verbose_name=_("Feature"),
        help_text=_("Related feature."),
    )
