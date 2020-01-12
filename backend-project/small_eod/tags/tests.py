from .factories import TagFactory, TagNamespaceFactory
from .models import Tag, TagNamespace
from ..tests.factories import FactoryTestCase
from django.test import TestCase


class TagsFactoryTestCase(FactoryTestCase):

    FACTORIES = (
        (Tag, TagFactory),
        (TagNamespace, TagNamespaceFactory)
    )


class TagsTestCase(TestCase):

    def test_prefix(self):
        tag = TagFactory(name="test")
        tag_namespace = TagNamespaceFactory(prefix="test")
        tag.save(), tag_namespace.save()
        self.assertTrue(tag.name.startswith(tag_namespace.prefix))
