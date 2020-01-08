from django.db import models
from ..generic.models import TimestampUserLogModel
from ..cases.models import Case


class DictTypes(models.TextChoices):
    WHOSE = "WHOSE", "Do kogo należy sprawa"
    WSCOPE = "WSCOPE", "Jaki zakres sprawy"
    ISCOPE = "ISCOPE", "Bezczynność w jakim zakresie"
    DSCOPE = "DSCOPE", "Decyzja w jakim zakresie"
    INFOT = "INFOT", "Informacja udzielona w którym momencie"
    STATUS = "STATUS", "Status"


class Dictionary(TimestampUserLogModel):
    case = models.ForeignKey(to=Case, on_delete=models.CASCADE)
    type = models.CharField(max_length=6, choices=DictTypes.choices)
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Dictionaries"


class ChoiceRange(models.Model):
    case = models.ForeignKey(to=Case, on_delete=models.CASCADE)
    type = models.CharField(max_length=6, choices=DictTypes.choices)
    minItems = models.IntegerField(default=1)
    maxItems = models.IntegerField(default=1)

    class Meta:
        unique_together = ('type', 'case')
