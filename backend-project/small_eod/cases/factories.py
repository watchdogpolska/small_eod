import factory

from .models import Case
from ..features.factories import FeatureOptionFactory
from ..tags.factories import TagFactory
from ..institutions.factories import InstitutionFactory
from ..users.factories import UserFactory
from ..generic.factories import (
    AbstractTimestampUserFactory,
    ManyToManyPostGeneration,
)


class CaseFactory(AbstractTimestampUserFactory, factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: "case-%04d" % n)
    comment = factory.Sequence(lambda n: "comment-%04d" % n)
    audited_institutions = ManyToManyPostGeneration(
        m2m_field_name="audited_institutions", factory_cls=InstitutionFactory
    )
    responsible_users = ManyToManyPostGeneration(
        m2m_field_name="responsible_users", factory_cls=UserFactory
    )
    notified_users = ManyToManyPostGeneration(
        m2m_field_name="notified_users", factory_cls=UserFactory
    )
    tags = ManyToManyPostGeneration(
        m2m_field_name="tags", factory_cls=TagFactory, size=3
    )
    featureoptions = ManyToManyPostGeneration(
        m2m_field_name="featureoptions", factory_cls=FeatureOptionFactory
    )

    class Meta:
        model = Case
