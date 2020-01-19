from django.test import TestCase

from ..factories import DictionaryFactory, FeatureFactory
from ..models import Dictionary, Feature
from ...generic.tests import FactoryCreateObjectsMixin


class DictionaryFactoryTestCase(FactoryCreateObjectsMixin, TestCase):
    MODEL = Dictionary
    FACTORY = DictionaryFactory


class FeatureFactoryTestCase(FactoryCreateObjectsMixin, TestCase):
    MODEL = Feature
    FACTORY = FeatureFactory

    def test_foreign_keys(self):
        """
        Foreign keys are created.
        """
        obj = self.create_factory()
        self.assertIsNotNone(obj.dictionary)
