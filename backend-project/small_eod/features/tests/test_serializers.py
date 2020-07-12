from django.test import TestCase

from ..models import FeatureOption
from ..serializers import FeatureSerializer
from ...generic.mixins import AuthRequiredMixin
from ...generic.tests.test_serializers import ResourceSerializerMixin
from ..factories import FeatureFactory


class FeatureSerializerTestCase(ResourceSerializerMixin, AuthRequiredMixin, TestCase):
    serializer_class = FeatureSerializer
    factory_class = FeatureFactory

    def get_serializer_context(self):
        return {"request": self.request}

    def test_save_nested_values(self):
        self.login_required()
        serializer = FeatureSerializer(
            data={
                "name": "Czyja sprawa",
                "min_options": 1,
                "max_options": 2,
                "featureoptions": [{"name": "SO-WP"}, {"name": "Klienci"}],
            },
            context=self.get_serializer_context(),
        )
        self.assertTrue(serializer.is_valid(), serializer.errors)
        feature = serializer.save()
        self.assertTrue(FeatureOption.objects.count(), 2)
        self.assertEqual(FeatureOption.objects.first().feature, feature)
