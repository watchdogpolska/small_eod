from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel


class Case(TimeStampedModel):
    name = models.CharField(max_length=100, verbose_name="Name")
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created']


class Institution(TimeStampedModel):
    name = models.CharField(max_length=100, verbose_name="Name")
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created']


class Letter(TimeStampedModel):
    name = models.CharField(max_length=200, verbose_name="Description")
    direction = models.CharField(max_length=50, choices=(("R", "received"),
                                                         ("S", "send")))
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    data = models.DateField(verbose_name="Date of receipt / Date of dispatch")
    identifier = models.CharField(max_length=10, verbose_name="Identifier")
    case = models.ForeignKey(Case, on_delete=models.SET_NULL, null=True, blank=True)
    attachment = models.FileField()
    ordering = models.IntegerField(default=1, blank=True)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['data', ]