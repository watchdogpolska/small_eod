from django.conf import settings
from django.db import models
from model_utils import Choices
from model_utils.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _


class Dictionary(TimeStampedModel):
    TYPE = Choices((1, 'whose_case', _("Whose case")),
                   (2, 'what_scope', _("What scope")),
                   (3, 'inaction_scope', _("Inaction scope")),
                   (4, 'decision_scope', _("Decision scope")),
                   (5, 'time_of_info_provide', _("The moment of providing information")),
                   (6, 'proceedings_interrupted', _("Proceedings interrupted")),
                   (7, 'status', _("Status"))
                   )
    type = models.IntegerField(choices=TYPE, verbose_name=_("Type"))
    name = models.CharField(max_length=100, verbose_name=_("Name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Dictionary")
        verbose_name_plural = _("Dictinaries")


class Case(TimeStampedModel):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    comment = models.TextField(blank=True, verbose_name=_("Comment"))
    responsible_people = models.ManyToManyField(to='cases.Person',
                                                blank=True,
                                                verbose_name=_("Responsble person"))
    tags = models.ManyToManyField(to="cases.Tag", verbose_name=_("Tags"), blank=True)

    whose_case = models.ManyToManyField(to=Dictionary,
                                        limit_choices_to={'type': Dictionary.TYPE.whose_case},
                                        verbose_name=_("Whose case"),
                                        blank=True,
                                        related_name="case_whose_case")
    what_scope = models.ManyToManyField(to=Dictionary,
                                        limit_choices_to={'type': Dictionary.TYPE.what_scope},
                                        verbose_name=_("What scope"),
                                        blank=True,
                                        related_name="case_what_scope")
    inaction_scope = models.ManyToManyField(to=Dictionary,
                                            limit_choices_to={'type': Dictionary.TYPE.inaction_scope},
                                            verbose_name=_("Inaction scope"),
                                            blank=True,
                                            related_name="case_inaction_scope"
                                            )
    decision_scope = models.ManyToManyField(to=Dictionary,
                                            limit_choices_to={'type': Dictionary.TYPE.decision_scope},
                                            verbose_name=_("Decision scope"),
                                            blank=True,
                                            related_name="case_decision_scope"
                                            )
    time_of_info_provide = models.ManyToManyField(to=Dictionary,
                                                  limit_choices_to={'type': Dictionary.TYPE.time_of_info_provide},
                                                  verbose_name=_("The moment of providing information"),
                                                  blank=True,
                                                  related_name="case_time_of_info_provide"
                                                  )
    proceddings_interrupted = models.ManyToManyField(to=Dictionary,
                                                     limit_choices_to={'type': Dictionary.TYPE.proceedings_interrupted},
                                                     verbose_name=_("Proceedings interrupted"),
                                                     blank=True,
                                                     related_name="case_proceedings_interrupted")
    status = models.ManyToManyField(to=Dictionary,
                                    limit_choices_to={'type': Dictionary.TYPE.status},
                                    verbose_name=_("Status"),
                                    blank=True,
                                    related_name="case_status")

    @staticmethod
    def autocomplete_search_fields():
        return "id__iexact", "name__icontains",

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created']
        verbose_name = _("Case")
        verbose_name_plural = _("Cases")


class Channel(TimeStampedModel):
    name = models.CharField(verbose_name=_("Name"), max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Channel")
        verbose_name_plural = _("Channels")


class Person(TimeStampedModel):
    name = models.CharField(max_length=100, verbose_name=_("Nazwa"))
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)

    @staticmethod
    def autocomplete_search_fields():
        return "id__iexact", "name__icontains",

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _("Persons")


class Tag(TimeStampedModel):
    name = models.CharField(verbose_name=_("Name"), max_length=100, unique=True)

    @staticmethod
    def autocomplete_search_fields():
        return "id__iexact", "name__icontains",

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class Institution(TimeStampedModel):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    comment = models.TextField(blank=True, verbose_name=_("Comment"))
    tags = models.ManyToManyField(to=Tag, verbose_name=_("Tags"), blank=True)

    @staticmethod
    def autocomplete_search_fields():
        return "id__iexact", "name__icontains",

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
                                    verbose_name=_("Institution"),
                                    null=True,
                                    on_delete=models.SET_NULL)
    data = models.DateField(verbose_name=_("Date of receipt / Date of dispatch"))
    identifier = models.CharField(max_length=100,
                                  verbose_name=_("Identifier"),
                                  blank=True)
    case = models.ForeignKey(to=Case,
                             on_delete=models.SET_NULL,
                             null=True,
                             blank=True,
                             verbose_name=_("Case"))
    attachment = models.FileField(verbose_name=_("Attachment"))
    ordering = models.IntegerField(default=1, blank=True, verbose_name=_("Ordering"))
    comment = models.TextField(blank=True, verbose_name=_("Comment"))
    tags = models.ManyToManyField(to=Tag, verbose_name=_("Tags"), blank=True)
    channel = models.ForeignKey(to=Channel, verbose_name=_("Channel"),
                                null=True, blank=True,
                                on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['data', ]
        verbose_name = _("Letter")
        verbose_name_plural = _("Letters")
