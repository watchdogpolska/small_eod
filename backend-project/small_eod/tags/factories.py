import factory
from factory.django import DjangoModelFactory
from factory.fuzzy import BaseFuzzyAttribute

from .models import Tag, TagNamespace
from ..users.factories import UserFactory


class ColorFuzzyAttribute(BaseFuzzyAttribute):
    def fuzz(self):
        n = factory.random.randgen.randint(0, 999999)
        return "{:06d}".format(n)


class TagFactory(DjangoModelFactory):
    name = factory.Sequence(lambda n: "tag-%s" % n)

    class Meta:
        model = Tag


class TagNamespaceFactory(DjangoModelFactory):
    prefix = factory.Sequence(lambda n: "tag-%s" % n)
    description = factory.Sequence(lambda n: "desc-%s" % n)
    color = ColorFuzzyAttribute()

    created_by = factory.SubFactory(UserFactory)
    modified_by = factory.SubFactory(UserFactory)

    class Meta:
        model = TagNamespace
