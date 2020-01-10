from django.test import TestCase
from .models import Feature
from .serializers import DictionarySerializer
# Create your tests here.
class DictionarySerializerTestCase(TestCase):
    def test_save_nested_values(self):
        serializer = DictionarySerializer(data={
            "name": "Czyja sprawa",
            "active": True,
            "min_items": 1,
            "max_items": 2,
            "values": [
                { "name": "SO-WP"},
                { "name": "Klienci"},
            ]
        })
        self.assertTrue(serializer.is_valid(), serializer.errors)
        dictionary = serializer.save()
        self.assertTrue(Feature.objects.count(), 2)
        self.assertEqual(Feature.objects.first().dictionary, dictionary)