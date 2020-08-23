from django.test import TestCase

from ..factories import FeatureFactory, FeatureOptionFactory
from ..models import Feature, FeatureOption
from ...generic.tests.mixins import FactoryTestCaseMixin


class FeatureFactoryTestCase(FactoryTestCaseMixin, TestCase):
    MODEL = Feature
    FACTORY = FeatureFactory


class FeatureOptionFactoryTestCase(FactoryTestCaseMixin, TestCase):
    MODEL = FeatureOption
    FACTORY = FeatureOptionFactory

    def test_foreign_keys(self):
        """
        Foreign keys are created.
        """
        obj = self.create_factory()
        self.assertIsNotNone(obj.feature)
