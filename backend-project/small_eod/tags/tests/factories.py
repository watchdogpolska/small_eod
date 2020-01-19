from django.test import TestCase

from ..factories import TagFactory, TagNamespaceFactory
from ..models import Tag, TagNamespace
from ...generic.tests import FactoryCreateObjectsMixin


class TagFactoryTestCase(FactoryCreateObjectsMixin, TestCase):
    MODEL = Tag
    FACTORY = TagFactory


class TagNamespaceFactoryTestCase(FactoryCreateObjectsMixin, TestCase):
    MODEL = TagNamespace
    FACTORY = TagNamespaceFactory
