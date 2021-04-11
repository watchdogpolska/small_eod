from test_plus.test import TestCase

from ...generic.tests.test_views import GenericViewSetMixin, OrderingViewSetMixin
from ...search.tests.mixins import SearchQueryMixin
from ..factories import TagFactory
from ..serializers import TagSerializer


class TagViewSetTestCase(GenericViewSetMixin, SearchQueryMixin, TestCase):
    basename = "tag"
    serializer_class = TagSerializer
    factory_class = TagFactory

    def get_create_data(self):
        return {"name": f"{self.obj.name}-created"}

    def validate_item(self, item):
        self.assertEqual(item["name"], self.obj.name)

    def validate_create_item(self, item):
        self.assertEqual(item["name"], f"{self.obj.name}-created")
