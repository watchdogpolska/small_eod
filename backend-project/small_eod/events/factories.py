import factory.fuzzy

from .models import Event
from ..cases.factories import CaseFactory
from ..generic.factories import AbstractTimestampUserFactory, FuzzyDateTimeFromNow


class EventFactory(AbstractTimestampUserFactory, factory.DjangoModelFactory):

    case = factory.SubFactory(CaseFactory)
    date = FuzzyDateTimeFromNow(max_days=10)
    name = factory.Sequence(lambda n: "event-%04d" % n)
    comment = factory.Sequence(lambda n: "comment-event-%04d" % n)

    class Meta:
        model = Event
