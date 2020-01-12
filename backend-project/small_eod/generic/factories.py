import factory

from ..users.factories import UserFactory


class AbstractTimestampUserFactory(factory.Factory):
    created_by = factory.SubFactory(UserFactory)
    modified_by = factory.SubFactory(UserFactory)

    class Meta:
        abstract = True
