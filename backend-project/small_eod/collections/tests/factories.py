from django.test import TestCase

from ..factories import CollectionFactory
from ..models import Collection
from ...generic.tests import FactoryCreateObjectsMixin


class CollectionFactoryTestCase(FactoryCreateObjectsMixin, TestCase):
    FACTORY = CollectionFactory
    MODEL = Collection
