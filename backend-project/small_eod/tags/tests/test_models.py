from django.test import TestCase

from ..factories import TagFactory, TagNamespaceFactory


class TagTestCase(TestCase):
    def test_prefix(self):
        """
        `Tag` can be matched by `TagNamespace.prefix`.
        """
        tag = TagFactory(name="test")
        tag_namespace = TagNamespaceFactory(prefix="test")
        self.assertTrue(tag.name.startswith(tag_namespace.prefix))
