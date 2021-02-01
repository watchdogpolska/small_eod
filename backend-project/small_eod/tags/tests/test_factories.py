from django.test import TestCase

from ...generic.tests.mixins import FactoryTestCaseMixin
from ..factories import TagFactory, TagNamespaceFactory
from ..models import Tag, TagNamespace


class TagFactoryTestCase(FactoryTestCaseMixin, TestCase):
    MODEL = Tag
    FACTORY = TagFactory


class TagNamespaceFactoryTestCase(FactoryTestCaseMixin, TestCase):
    MODEL = TagNamespace
    FACTORY = TagNamespaceFactory
