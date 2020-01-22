from django.test import TestCase

from ..factories import CollectionFactory
from ..models import Collection
from ...generic.tests.mixins import FactoryTestCaseMixin


class CollectionFactoryTestCase(FactoryTestCaseMixin, TestCase):
    FACTORY = CollectionFactory
    MODEL = Collection
