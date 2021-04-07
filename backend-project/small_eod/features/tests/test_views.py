from test_plus.test import TestCase

from ...generic.tests.test_views import GenericViewSetMixin, OrderingViewSetMixin
from ..factories import FeatureFactory, FeatureOptionFactory
from ..serializers import FeatureOptionSerializer, FeatureSerializer


class FeatureViewSetTestCase(GenericViewSetMixin, OrderingViewSetMixin, TestCase):
    basename = "feature"
    serializer_class = FeatureSerializer
    factory_class = FeatureFactory
    ordering_fields = ["-name", "min_options", "max_options,id"]

    def validate_item(self, item):
        self.assertEqual(item["name"], self.obj.name)

    def test_create_minimum(self):
        self.login_required()
        name = "testowa-nazwa"
        response = self.client.post(
            self.get_url(name="list", **self.get_extra_kwargs()),
            data={"name": name},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201, response.json())
        item = response.json()
        self.assertEqual(item["name"], name)


class FeatureOptionViewSetTestCase(GenericViewSetMixin, TestCase):
    basename = "feature_option"
    factory_class = FeatureOptionFactory
    serializer_class = FeatureOptionSerializer

    def validate_item(self, item):
        self.assertEqual(self.obj.name, item["name"])

    def increase_list(self):
        self.factory_class.create_batch(feature=self.obj.feature, size=5)
