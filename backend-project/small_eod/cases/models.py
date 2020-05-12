from django.db import models
from django.conf import settings

from ..institutions.models import Institution
from ..generic.models import TimestampUserLogModel
from ..features.models import FeatureOption
from ..tags.models import Tag
from django.utils.translation import ugettext_lazy as _


class CaseQuerySet(models.QuerySet):
    def with_counter(self):
        return self.annotate(
            letter_count=models.Count("letter"), note_count=models.Count("note")
        )


class Case(TimestampUserLogModel):
    objects = CaseQuerySet.as_manager()

    name = models.CharField(
        max_length=256, verbose_name=_("Name"), help_text=_("Case's name."),
    )
    comments = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=_("Comments"),
        help_text=_("Comments for this case."),
    )

    tags = models.ManyToManyField(
        to=Tag, blank=True, verbose_name=_("Tags"), help_text=_("Choose tags.")
    )
    featureoptions = models.ManyToManyField(
        to=FeatureOption,
        blank=True,
        verbose_name=_("Feature options"),
        help_text=_("Features options for this case."),
    )

    audited_institutions = models.ManyToManyField(
        to=Institution,
        blank=True,
        verbose_name="Audited institutions",
        help_text=_("Case audits this Institutions."),
    )
    notified_users = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        related_name="notified_users",
        blank=True,
        verbose_name=_("Notified users"),
        help_text=_("Users who will receive notifications."),
    )
    responsible_users = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        related_name="responsible_users",
        blank=True,
        verbose_name=_("Responsible users"),
        help_text=_("Users who is responsible for this case."),
    )

    def __str__(self):
        return self.name
