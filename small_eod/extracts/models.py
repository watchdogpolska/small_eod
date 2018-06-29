from django.db import models
from model_utils.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _


class Mail(TimeStampedModel):
    subject = models.TextField()
    to_address = models.TextField()
    from_address = models.TextField()
    body = models.TextField()
    text = models.TextField()
    attachments_count = models.TextField()
    date = models.TextField()

    class Meta:
        verbose_name = _("Mails")
        verbose_name_plural = _("Mails")