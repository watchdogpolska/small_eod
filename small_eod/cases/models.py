from django.db import models
from model_utils.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _


class Case(TimeStampedModel):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    comment = models.TextField(blank=True, verbose_name=_("Comment"))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created']
        verbose_name = _("Case")
        verbose_name_plural = _("Cases")


class Institution(TimeStampedModel):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    comment = models.TextField(blank=True, verbose_name=_("Comment"))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created']
        verbose_name = _("Institution")
        verbose_name_plural = _("Institutions")


class Letter(TimeStampedModel):
    DIRECTION = (
        ("R", _("received")),
        ("S", _("send"))
    )
    name = models.CharField(max_length=200, verbose_name=_("Description"))
    direction = models.CharField(max_length=50, choices=DIRECTION,
                                 verbose_name=_("Direction"))
    institution = models.ForeignKey(to=Institution,
                                    on_delete=models.CASCADE,
                                    verbose_name=_("Institution"))
    data = models.DateField(verbose_name=_("Date of receipt / Date of dispatch"))
    identifier = models.CharField(max_length=10,
                                  verbose_name=_("Identifier"))
    case = models.ForeignKey(to=Case,
                             on_delete=models.SET_NULL,
                             null=True,
                             blank=True,
                             verbose_name=_("Case"))
    attachment = models.FileField(verbose_name=_("Attachment"))
    ordering = models.IntegerField(default=1, blank=True, verbose_name=_("Ordering"))
    comment = models.TextField(blank=True, verbose_name=_("Comment"))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['data', ]
        verbose_name = _("Letter")
        verbose_name_plural = _("Letters")
