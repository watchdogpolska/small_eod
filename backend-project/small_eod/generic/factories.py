import factory

from ..users.factories import UserFactory


class TimestampUserFactoryMixin:
    created_by = factory.SubFactory(UserFactory)
    modified_by = factory.SubFactory(UserFactory)
