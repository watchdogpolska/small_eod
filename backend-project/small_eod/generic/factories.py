import datetime
import string

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


class PolishFaker(factory.Faker):
    def __init__(self, *args, **kwargs):
        kwargs["locale"] = "PL"
        super().__init__(*args, **kwargs)


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


class FuzzyRegon(factory.fuzzy.BaseFuzzyAttribute):
    def __init__(self):
        super().__init__()
        self.chars_10 = factory.fuzzy.FuzzyText(length=10, chars=string.digits)
        self.chars_14 = factory.fuzzy.FuzzyText(length=14, chars=string.digits)

    def fuzz(self):
        return factory.random.randgen.choice([self.chars_10, self.chars_14]).fuzz()


class RGBColorFuzzyAttribute(factory.fuzzy.BaseFuzzyAttribute):
    def fuzz(self):
        n = factory.random.randgen.randint(0, 999999)
        return f"{n:06d}"
