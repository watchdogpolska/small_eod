from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..features.models import FeatureOption
from ..generic.models import TimestampUserLogModel
from ..institutions.models import Institution
from ..tags.models import Tag


class CaseQuerySet(models.QuerySet):
    def with_counter(self):
        return self.annotate(
            letter_count=models.Count("letter"), note_count=models.Count("note")
        )

    def with_nested_resources(self):
        return (
            self.prefetch_related("featureoptions")
            .prefetch_related("responsible_users")
            .prefetch_related("notified_users")
            .prefetch_related("audited_institutions")
            .prefetch_related("tags")
        )


class Case(TimestampUserLogModel):
    objects = CaseQuerySet.as_manager()

    name = models.CharField(
        max_length=256,
        verbose_name=_("Name"),
        help_text=_("Case's name."),
    )
    comment = models.TextField(
        blank=True,
        verbose_name=_("Comment"),
        help_text=_("Comment for this case."),
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
        related_name="notified_about_case_set",
        blank=True,
        verbose_name=_("Notified users"),
        help_text=_("Users who will receive notifications."),
    )
    responsible_users = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        related_name="responsible_for_case_set",
        blank=True,
        verbose_name=_("Responsible users"),
        help_text=_("Users who is responsible for this case."),
    )

    @staticmethod
    def autocomplete_search_fields():
        return (
            "id__iexact",
            "name__icontains",
        )

    def __str__(self):
        return self.name
