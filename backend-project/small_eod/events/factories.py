import factory.fuzzy
from factory.django import DjangoModelFactory

from ..cases.factories import CaseFactory
from ..generic.factories import AbstractTimestampUserFactory, FuzzyDateTimeFromNow
from .models import Event


class EventFactory(AbstractTimestampUserFactory, DjangoModelFactory):

    case = factory.SubFactory(CaseFactory)
    date = FuzzyDateTimeFromNow(max_days=10)
    name = factory.Sequence(lambda n: "event-%04d" % n)
    comment = factory.Sequence(lambda n: "comments-event-%04d" % n)

    class Meta:
        model = Event
