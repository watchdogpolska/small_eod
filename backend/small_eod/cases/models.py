from django.db import models
from django.conf import settings

from ..institutions.models import Institution
from ..generic.models import TimestampUserLogModel
from ..dictionaries.models import Feature
from ..tags.models import Tag


class CaseQuerySet(models.QuerySet):
    def with_counter(self):
        return self.annotate(letter_count=models.Count("letter"), note_count=models.Count("note"))

class Case(TimestampUserLogModel):
    name = models.CharField(max_length=256)
    comment = models.CharField(max_length=256)
    auditedInstitution = models.ManyToManyField(to=Institution, blank=True)
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
    feature = models.ManyToManyField(to=Feature, blank=True)
    tag = models.ManyToManyField(to=Tag, blank=True)

    objects = CaseQuerySet.as_manager()