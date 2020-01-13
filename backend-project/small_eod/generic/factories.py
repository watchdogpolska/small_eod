import datetime

import factory.fuzzy
from django.utils import timezone

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


class FuzzyTrueOrFalse(factory.fuzzy.FuzzyChoice):
    def __init__(self, **kwargs):
        kwargs["choices"] = (True, False)
        super().__init__(**kwargs)


class FuzzyTrueOrFalseOrNone(factory.fuzzy.FuzzyChoice):
    def __init__(self, **kwargs):
        kwargs["choices"] = (True, False, None)
        super().__init__(**kwargs)


class FuzzyDateTimeFromNow(factory.fuzzy.FuzzyDateTime):
    def __init__(self, max_days: int = None, **kwargs):
        kwargs["start_dt"] = timezone.now()
        kwargs["end_dt"] = timezone.now() + datetime.timedelta(days=max_days)
        super().__init__(**kwargs)
