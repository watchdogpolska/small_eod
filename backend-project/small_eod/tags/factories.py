import factory
from factory.django import DjangoModelFactory
from factory.fuzzy import BaseFuzzyAttribute

from .models import Tag, TagNamespace
from ..generic.factories import AbstractTimestampUserFactory


class ColorFuzzyAttribute(BaseFuzzyAttribute):
    def fuzz(self):
        n = factory.random.randgen.randint(0, 999999)
        return "{:06d}".format(n)


class TagFactory(DjangoModelFactory):
    name = factory.Sequence(lambda n: "tag-%04d" % n)

    class Meta:
        model = Tag


class TagNamespaceFactory(AbstractTimestampUserFactory, DjangoModelFactory):
    prefix = factory.Sequence(lambda n: "tag-%04d" % n)
    description = factory.Sequence(lambda n: "desc-%04d" % n)
    color = ColorFuzzyAttribute()

    class Meta:
        model = TagNamespace
