import factory.fuzzy

from .models import Event
from ..cases.factories import CaseFactory
from ..generic.factories import AbstractTimestampUserFactory, FuzzyDateTimeFromNow


class EventFactory(AbstractTimestampUserFactory, factory.DjangoModelFactory):

    cases = factory.SubFactory(CaseFactory)
    date = FuzzyDateTimeFromNow(max_days=10)
    name = factory.Sequence(lambda n: "event-%04d" % n)
    comments = factory.Sequence(lambda n: "comments-event-%04d" % n)

    class Meta:
        model = Event
