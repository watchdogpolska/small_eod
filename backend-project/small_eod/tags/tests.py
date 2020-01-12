from django.test import TestCase

from .factories import TagFactory, TagNamespaceFactory
from .models import Tag, TagNamespace
from ..generic.tests import FactoryCreateObjectsMixin


class TagFactoryTestCase(FactoryCreateObjectsMixin, TestCase):
    MODEL = Tag
    FACTORY = TagFactory


class TagNamespaceFactoryTestCase(FactoryCreateObjectsMixin, TestCase):
    MODEL = TagNamespace
    FACTORY = TagNamespaceFactory


class TagsTestCase(TestCase):

    def test_prefix(self):
        """
        `Tag` can be matched by `TagNamespace.prefix`.
        """
        tag = TagFactory(name="test")
        tag_namespace = TagNamespaceFactory(prefix="test")
        self.assertTrue(tag.name.startswith(tag_namespace.prefix))


class TagNamespaceTestCase(TestCase):
    pass
