import factory

from ..users.factories import UserFactory


def _m2m_post_add(attr, obj, create, extracted, **kwargs):
    if not create:
        return
    if extracted:
        getattr(obj, attr).set(extracted)


class AbstractTimestampUserFactory(factory.Factory):
    created_by = factory.SubFactory(UserFactory)
    modified_by = factory.SubFactory(UserFactory)

    class Meta:
        abstract = True


class ManyToManyPostGeneration(factory.PostGeneration):
    def __init__(self, m2m_field_name):
        super().__init__(function=None)
        self.m2m_field_name = m2m_field_name
        self.function = lambda obj, create, extracted, **kwargs: _m2m_post_add(
            attr=self.m2m_field_name,
            obj=obj,
            create=create,
            extracted=extracted,
            **kwargs,
        )
