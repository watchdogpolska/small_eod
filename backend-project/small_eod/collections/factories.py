import factory
import factory.fuzzy
from django.utils import timezone
import datetime
from .models import Collection


class CollectionFactory(factory.django.DjangoModelFactory):
    comment = factory.Sequence(lambda n: "comment-%04d" % n)
    public = True
    expired_on = factory.fuzzy.FuzzyDateTime(
        start_dt=timezone.now(), end_dt=timezone.now() + datetime.timedelta(days=10)
    )

    class Meta:
        model = Collection
