import factory.fuzzy

from .models import FeatureOption, Feature
from ..generic.factories import AbstractTimestampUserFactory, FuzzyTrueOrFalse


class FeatureFactory(AbstractTimestampUserFactory, factory.django.DjangoModelFactory):
    min_options = factory.fuzzy.FuzzyInteger(1, 3)
    max_options = factory.fuzzy.FuzzyInteger(3, 20)
    name = factory.Sequence(lambda n: "feature-%04d" % n)

    class Meta:
        model = Feature


class FeatureOptionFactory(factory.django.DjangoModelFactory):
    feature = factory.SubFactory(FeatureFactory)
    name = factory.Sequence(lambda n: "featureoption-%04d" % n)

    class Meta:
        model = FeatureOption
