from django.test import TestCase

from ..factories import TagFactory, TagNamespaceFactory
from ..models import Tag, TagNamespace
from ...generic.tests.mixins import FactoryTestCaseMixin


class TagFactoryTestCase(FactoryTestCaseMixin, TestCase):
    MODEL = Tag
    FACTORY = TagFactory


class TagNamespaceFactoryTestCase(FactoryTestCaseMixin, TestCase):
    MODEL = TagNamespace
    FACTORY = TagNamespaceFactory
