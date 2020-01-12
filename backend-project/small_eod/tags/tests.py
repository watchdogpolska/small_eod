from django.test import TestCase

from .factories import TagFactory, TagNamespaceFactory
from .models import Tag, TagNamespace
from ..generic.tests import FactoryTestCase


class TagFactoryTestCase(FactoryTestCase):

    FACTORIES = [
        (Tag, TagFactory)
    ]


class TagNamespaceFactoryTestCase(FactoryTestCase):

    FACTORIES = [
        (TagNamespace, TagNamespaceFactory)
    ]

class TagsTestCase(TestCase):

    def test_prefix(self):
        tag = TagFactory(name="test")
        tag_namespace = TagNamespaceFactory(prefix="test")
        self.assertTrue(tag.name.startswith(tag_namespace.prefix))
