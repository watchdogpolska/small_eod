from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..letters.models import Letter


class File(models.Model):
    path = models.CharField(
        max_length=355, verbose_name=_("Path"), help_text=_("Path to file.")
    )
    name = models.CharField(
        max_length=255, verbose_name=_("Name"), help_text=_("Name of file.")
    )
    letter = models.ForeignKey(
        to=Letter,
        on_delete=models.CASCADE,
        related_name="attachments",
        verbose_name=_("Letter"),
        help_text=_("Related letter."),
    )

    def __str__(self):
        return self.name
