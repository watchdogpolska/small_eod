import factory
from factory.django import DjangoModelFactory

from .models import Tag, TagNamespace
from ..generic.factories import AbstractTimestampUserFactory, RGBColorFuzzyAttribute


class TagFactory(DjangoModelFactory):
    name = factory.Sequence(lambda n: "tag-%04d" % n)

    class Meta:
        model = Tag
        django_get_or_create = ("name",)


class TagNamespaceFactory(AbstractTimestampUserFactory, DjangoModelFactory):

    color = RGBColorFuzzyAttribute()
    prefix = factory.Sequence(lambda n: "tag-%04d" % n)
    description = factory.Sequence(lambda n: "desc-%04d" % n)

    class Meta:
        model = TagNamespace
