from django.db import models
from generic.models import TimestampUserLogModel
from case.models import Case


class DictTypes(models.TextChoices):
    WHOSE = "WHOSE", "Do kogo należy sprawa"
    WSCOPE = "WSCOPE", "Jaki zakres sprawy"
    ISCOPE = "ISCOPE", "Bezczynność w jakim zakresie"
    DSCOPE = "DSCOPE", "Decyzja w jakim zakresie"
    INFOT = "INFOT", "Informacja udzielona w którym momencie"
    STATUS = "STATUS", "Status"


class Dictionary(TimestampUserLogModel):
    type = models.CharField(max_length=6, choices=DictTypes.choices)
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    case = models.ForeignKey(to=Case, on_delete=models.CASCADE)


class ChoiceRange(models.Model):
    type = models.CharField(max_length=6, choices=DictTypes.choices)
    minItems = models.IntegerField(default=1)
    maxItems = models.IntegerField(default=1)
    case = models.ForeignKey(to=Case, on_delete=models.CASCADE)
