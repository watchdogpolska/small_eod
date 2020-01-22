from django.db import models
from django.conf import settings

from ..institutions.models import Institution
from ..generic.models import TimestampUserLogModel
from ..dictionaries.models import Feature
from ..tags.models import Tag
from django.utils.translation import ugettext_lazy as _


class CaseQuerySet(models.QuerySet):
    def with_counter(self):
        return self.annotate(
            letter_count=models.Count("letter"), note_count=models.Count("note")
        )


class Case(TimestampUserLogModel):
    objects = CaseQuerySet.as_manager()

    name = models.CharField(max_length=256, verbose_name=_("Name"),
                            help_text=_("Case's name. Name cannot be longer than 256 characters.")
                            )
    comment = models.CharField(max_length=256, verbose_name=_("Comment"),
                               help_text=_("Comment cannot be longer than 256 characters.")
                               )

    tag = models.ManyToManyField(to=Tag, blank=True, verbose_name=_("Tag"), help_text="Choose tag.")
    feature = models.ManyToManyField(to=Feature, blank=True, verbose_name=_("Feature"))

    audited_institution = models.ManyToManyField(
        to=Institution, blank=True,
        verbose_name="Audited institution", help_text=_("Case audits this Institution."),
    )
    notified_user = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL, related_name="case_notified_user", blank=True,
        verbose_name=_("Notified user"), help_text=_("User who will receive notification.")
    )
    responsible_user = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL, related_name="case_responsible_user", blank=True,
        verbose_name=_("Responsible user"), help_text=_("User who is responsible for this case.")
    )

    def __str__(self):
        return self.name
