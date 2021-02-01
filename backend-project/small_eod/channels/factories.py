import factory.fuzzy
from factory.django import DjangoModelFactory

from ..generic.factories import AbstractTimestampUserFactory, FuzzyTrueOrFalse
from .models import Channel


class ChannelFactory(AbstractTimestampUserFactory, DjangoModelFactory):

    name = factory.Sequence(lambda n: "channel-%04d" % n)
    city = FuzzyTrueOrFalse()
    voivodeship = FuzzyTrueOrFalse()
    flat_no = FuzzyTrueOrFalse()
    street = FuzzyTrueOrFalse()
    postal_code = FuzzyTrueOrFalse()
    house_no = FuzzyTrueOrFalse()
    email = FuzzyTrueOrFalse()
    epuap = FuzzyTrueOrFalse()

    class Meta:
        model = Channel
