import factory

from .models import Case
from ..generic.factories import (
    AbstractTimestampUserFactory,
    ManyToManyPostGeneration,
)


class CaseFactory(AbstractTimestampUserFactory, factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: "case-%04d" % n)
    comment = factory.Sequence(lambda n: "comment-%04d" % n)
    audited_institutions = ManyToManyPostGeneration("audited_institution")
    responsible_users = ManyToManyPostGeneration("responsible_user")
    notified_users = ManyToManyPostGeneration("notified_user")
    tags = ManyToManyPostGeneration("tag")

    # todo
    # feature = ManyToManyPostGeneration("feature")
    class Meta:
        model = Case
