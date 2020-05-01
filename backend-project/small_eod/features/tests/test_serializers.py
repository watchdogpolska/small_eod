from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate

from ..models import FeatureOption
from ..serializers import FeatureSerializer
from ...users.factories import UserFactory


class FeatureSerializerTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        factory = APIRequestFactory()
        self.request = factory.get("/")
        force_authenticate(self.request, user=self.user)
        self.request.user = self.user

    def test_save_nested_values(self):
        serializer = FeatureSerializer(
            data={
                "name": "Czyja sprawa",
                "min_options": 1,
                "max_options": 2,
                "featureoptions": [{"name": "SO-WP"}, {"name": "Klienci"}],
            },
            context={"request": self.request},
        )
        self.assertTrue(serializer.is_valid(), serializer.errors)
        features = serializer.save()
        self.assertTrue(FeatureOption.objects.count(), 2)
        self.assertEqual(FeatureOption.objects.first().features, features)
