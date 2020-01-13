from django.test import TestCase

from .factories import DictionaryFactory, FeatureFactory
from .models import Dictionary, Feature
from .serializers import DictionarySerializer
from ..generic.tests import FactoryCreateObjectsMixin


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


class DictionarySerializerTestCase(TestCase):
    def test_save_nested_values(self):
        serializer = DictionarySerializer(
            data={
                "name": "Czyja sprawa",
                "active": True,
                "min_items": 1,
                "max_items": 2,
                "values": [{"name": "SO-WP"}, {"name": "Klienci"},],
            }
        )
        self.assertTrue(serializer.is_valid(), serializer.errors)
        dictionary = serializer.save()
        self.assertTrue(Feature.objects.count(), 2)
        self.assertEqual(Feature.objects.first().dictionary, dictionary)
