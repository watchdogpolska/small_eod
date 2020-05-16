from test_plus.test import TestCase

from ..factories import FeatureFactory, FeatureOptionFactory
from ..serializers import FeatureSerializer, FeatureOptionSerializer
from ...generic.tests.test_views import GenericViewSetMixin


class FeatureViewSetTestCase(GenericViewSetMixin, TestCase):
    basename = "feature"
    serializer_class = FeatureSerializer
    factory_class = FeatureFactory

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

    def test_create_with_featureoptions(self):
        self.login_required()
        name = "testowa-nazwa"
        optionname = "testowa-nazwa2"
        response = self.client.post(
            self.get_url(name="list", **self.get_extra_kwargs()),
            data={"name": name, "featureoptions": [{"name": optionname}]},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201, response.json())
        item = response.json()
        self.assertEqual(item["name"], name)
        self.assertEqual(item["featureoptions"][0]["name"], optionname)

    def test_num_queries_for_list(self):
        # TODO
        pass

    def test_num_queries_for_detail(self):
        # TODO
        pass


class FeatureOptionViewSetTestCase(GenericViewSetMixin, TestCase):
    basename = "feature-featureoption"
    factory_class = FeatureOptionFactory
    serializer_class = FeatureOptionSerializer
    queries_less_than_limit = 5

    def get_extra_kwargs(self):
        return dict(feature_pk=self.obj.features.pk)

    def validate_item(self, item):
        self.assertEqual(self.obj.name, item["name"])

    def test_num_queries_for_list(self):
        # TODO
        pass

    def test_num_queries_for_detail(self):
        # TODO
        pass
