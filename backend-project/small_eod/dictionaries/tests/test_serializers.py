from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate

from ..models import Feature
from ..serializers import DictionarySerializer
from ...users.factories import UserFactory


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
