import datetime

import factory.fuzzy
from django.utils import timezone

from .models import Collection
from ..generic.factories import AbstractTimestampUserFactory, FuzzyTrueOrFalse


class CollectionFactory(AbstractTimestampUserFactory, factory.DjangoModelFactory):
    # todo add `query` | improve `expired_on`

    comment = factory.Sequence(lambda n: "comment-%04d" % n)
    public = FuzzyTrueOrFalse()
    expired_on = factory.fuzzy.FuzzyDateTime(
        start_dt=timezone.now(), end_dt=timezone.now() + datetime.timedelta(days=10),
    )

    class Meta:
        model = Collection
