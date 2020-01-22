from django.test import TestCase

from ..factories import DictionaryFactory, FeatureFactory
from ..models import Dictionary, Feature
from ...generic.tests.mixins import FactoryTestCaseMixin


class DictionaryFactoryTestCase(FactoryTestCaseMixin, TestCase):
    MODEL = Dictionary
    FACTORY = DictionaryFactory


class FeatureFactoryTestCase(FactoryTestCaseMixin, TestCase):
    MODEL = Feature
    FACTORY = FeatureFactory

    def test_foreign_keys(self):
        """
        Foreign keys are created.
        """
        obj = self.create_factory()
        self.assertIsNotNone(obj.dictionary)
