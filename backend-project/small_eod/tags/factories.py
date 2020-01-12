import random

import factory
from factory.django import DjangoModelFactory

from .models import Tag, TagNamespace


class TagFactory(DjangoModelFactory):
    name = factory.Sequence(lambda n: "tag-%s" % n)

    class Meta:
        model = Tag


class TagNamespaceFactory(DjangoModelFactory):
    prefix = factory.Sequence(lambda n: "tag-%s" % n)
    description = factory.Sequence(lambda n: "desc-%s" % n)
    color = factory.Sequence(lambda n: "{:06d}".format(random.randint(0, 999999) + n))

    class Meta:
        model = TagNamespace
