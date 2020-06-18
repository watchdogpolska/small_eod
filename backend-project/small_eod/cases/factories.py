import factory

from .models import Case
from ..generic.factories import (
    AbstractTimestampUserFactory,
    ManyToManyPostGeneration,
)


class CaseFactory(AbstractTimestampUserFactory, factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: "case-%04d" % n)
    comment = factory.Sequence(lambda n: "comment-%04d" % n)
    audited_institutions = ManyToManyPostGeneration("audited_institutions")
    responsible_users = ManyToManyPostGeneration("responsible_users")
    notified_users = ManyToManyPostGeneration("notified_users")
    tags = ManyToManyPostGeneration("tags")
    featureoptions = ManyToManyPostGeneration("featureoptions")

    class Meta:
        model = Case
        django_get_or_create = ("pk",)
