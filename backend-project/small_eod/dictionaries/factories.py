import factory.fuzzy

from .models import Feature, Dictionary
from ..generic.factories import AbstractTimestampUserFactory


class DictionaryFactory(
    AbstractTimestampUserFactory, factory.django.DjangoModelFactory
):
    name = factory.Sequence(lambda n: "dictionary-%04d" % n)
    active = factory.fuzzy.FuzzyChoice((True, False))
    min_items = factory.fuzzy.FuzzyInteger(1, 3)
    max_items = factory.fuzzy.FuzzyInteger(3, 20)

    class Meta:
        model = Dictionary


class FeatureFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: "feature-%04d" % n)
    dictionary = factory.SubFactory(DictionaryFactory)

    class Meta:
        model = Feature
