from django.db import models
from ..letters.models import Letter
from django.utils.translation import ugettext_lazy as _


class File(models.Model):
    path = models.CharField(
        max_length=200, verbose_name=_("Path"), help_text=_("Path to file.")
    )
    name = models.CharField(
        max_length=100, verbose_name=_("Name"), help_text=_("Name of file.")
    )
    letters = models.ForeignKey(
        to=Letter,
        on_delete=models.CASCADE,
        related_name="attachments",
        verbose_name=_("Letters"),
        help_text=_("Related letters."),
    )
