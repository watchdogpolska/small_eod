import factory.fuzzy

from .models import Collection
from ..generic.factories import (
    AbstractTimestampUserFactory,
    FuzzyTrueOrFalse,
    FuzzyDateTimeFromNow,
)


class CollectionFactory(AbstractTimestampUserFactory, factory.DjangoModelFactory):
    # todo add `query`
    name = factory.Sequence(lambda n: "collection-%04d" % n)
    public = FuzzyTrueOrFalse()
    expired_on = FuzzyDateTimeFromNow(max_days=10)
    comment = factory.Sequence(lambda n: "comment-%04d" % n)
    query = "Some query"

    class Meta:
        model = Collection
