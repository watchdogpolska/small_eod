from test_plus.test import TestCase

from ...generic.tests.test_views import OrderingViewSetMixin, ReadOnlyViewSetMixin
from ...search.tests.mixins import SearchQueryMixin
from ..factories import AdministrativeUnitFactory
from ..serializers import AdministrativeUnitSerializer


class AdministrativeUnitViewSetTestCase(
    ReadOnlyViewSetMixin, OrderingViewSetMixin, SearchQueryMixin, TestCase
):
    basename = "administrative_unit"
    serializer_class = AdministrativeUnitSerializer
    factory_class = AdministrativeUnitFactory
    ordering_fields = [
        "category__level",
        "name",
        "-updated_on",
        "active,id",
    ]

    def validate_item(self, item):
        self.assertEqual(item["name"], self.obj.name)
