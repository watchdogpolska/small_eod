from django.test import TestCase

from .factories import DictionaryFactory, FeatureFactory
from .models import Dictionary, Feature
from .serializers import DictionarySerializer
from ..generic.tests import FactoryCreateObjectsMixin
from ..users.factories import UserFactory
from rest_framework.test import APIRequestFactory, force_authenticate


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
    def setUp(self):
        self.user = UserFactory()
        factory = APIRequestFactory()
        self.request = factory.get("/")
        force_authenticate(self.request, user=self.user)
        self.request.user = self.user

    def test_save_nested_values(self):
        serializer = DictionarySerializer(
            data={
                "name": "Czyja sprawa",
                "active": True,
                "min_items": 1,
                "max_items": 2,
                "values": [{"name": "SO-WP"}, {"name": "Klienci"}],
            },
            context={"request": self.request},
        )
        self.assertTrue(serializer.is_valid(), serializer.errors)
        dictionary = serializer.save()
        self.assertTrue(Feature.objects.count(), 2)
        self.assertEqual(Feature.objects.first().dictionary, dictionary)
