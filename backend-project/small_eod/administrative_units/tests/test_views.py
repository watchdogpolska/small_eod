from test_plus.test import TestCase

from ..factories import AdministrativeUnitFactory
from ..serializers import AdministrativeUnitSerializer
from ...generic.tests.test_views import ReadOnlyViewSetMixin


class AdministrativeUnitViewSetTestCase(ReadOnlyViewSetMixin, TestCase):
    basename = "administrative_unit"
    serializer_class = AdministrativeUnitSerializer
    factory_class = AdministrativeUnitFactory

    def validate_item(self, item):
        self.assertEqual(item["name"], self.obj.name)
