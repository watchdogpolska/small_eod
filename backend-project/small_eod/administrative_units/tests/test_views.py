from random import randint
from django.test import TestCase

from teryt_tree.factories import CategoryFactory
from ..factories import JednostkaAdministracyjnaFactory
from ..serializers import AdministrativeUnitSerializer
from ...generic.tests.test_views import ReadOnlyViewSetMixin


class CaseViewSetTestCase(ReadOnlyViewSetMixin, TestCase):
    basename = "administrative_unit"
    serializer_class = AdministrativeUnitSerializer
    factory_class = JednostkaAdministracyjnaFactory

    def validate_item(self, item):
        self.assertEqual(item["name"], self.obj.name)
