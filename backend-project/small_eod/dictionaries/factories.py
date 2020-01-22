import factory.fuzzy

from .models import Feature, Dictionary
from ..generic.factories import AbstractTimestampUserFactory, FuzzyTrueOrFalse


class DictionaryFactory(
    AbstractTimestampUserFactory, factory.django.DjangoModelFactory
):
    active = FuzzyTrueOrFalse()
    min_items = factory.fuzzy.FuzzyInteger(1, 3)
    max_items = factory.fuzzy.FuzzyInteger(3, 20)
    name = factory.Sequence(lambda n: "dictionary-%04d" % n)

    class Meta:
        model = Dictionary


class FeatureFactory(factory.django.DjangoModelFactory):

    dictionary = factory.SubFactory(DictionaryFactory)
    name = factory.Sequence(lambda n: "feature-%04d" % n)

    class Meta:
        model = Feature
