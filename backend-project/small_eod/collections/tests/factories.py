from django.test import TestCase

from ..factories import CollectionFactory
from ..models import Collection
from ...generic.tests.factories import FactoryTestCaseMixin


class CollectionFactoryTestCase(FactoryTestCaseMixin, TestCase):
    FACTORY = CollectionFactory
    MODEL = Collection
