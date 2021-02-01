from django.test import TestCase

from ...generic.tests.mixins import FactoryTestCaseMixin
from ..factories import CollectionFactory
from ..models import Collection


class CollectionFactoryTestCase(FactoryTestCaseMixin, TestCase):
    FACTORY = CollectionFactory
    MODEL = Collection
