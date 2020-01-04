from django.db import models
from django.conf import settings

from institution.models import Institution
from generic.models import TimestampUserLogModel


class Case(TimestampUserLogModel):
    comment = models.CharField(max_length=256)
    auditedInstitution = models.ManyToManyField(to=Institution)
    name = models.CharField(max_length=256)
    responsibleUser = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        related_name='case_responsibleUser',
        blank=True,
    )
    notifiedUser = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        related_name='case_notifiedUser',
        blank=True,
    )
    letterCount = models.IntegerField(default=0)
    noteCount = models.IntegerField(default=0)


