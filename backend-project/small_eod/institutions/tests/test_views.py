from django.test import TestCase

from ..factories import InstitutionFactory
from ..serializers import InstitutionSerializer
from ...generic.tests.test_views import (
    GenericViewSetMixin,
    AuthorshipViewSetMixin,
)


class InstitutionViewSetTestCase(AuthorshipViewSetMixin, GenericViewSetMixin, TestCase):
    basename = "institution"
    serializer_class = InstitutionSerializer
    factory_class = InstitutionFactory

    def validate_item(self, item):
        self.assertEqual(item["name"], self.obj.name)
