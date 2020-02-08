from django.test import TestCase

from ..factories import InstitutionFactory
from ..serializers import InstitutionSerializer
from ...generic.tests.test_views import (
    GenericViewSetMixin,
    ReadOnlyViewSetMixin,
    AuthorshipViewSetMixin,
)


class InstitutionViewSetTestCase(AuthorshipViewSetMixin, TestCase):
    # TODO - test nie przechodzi z powodu nieprawidłowego pk dla AdministrativeUnit podczas tworzenia, moim zdaniem problem leży po stronie Factory
    basename = "institution"
    serializer_class = InstitutionSerializer
    factory_class = InstitutionFactory

    def validate_item(self, item):
        self.assertEqual(item["name"], self.obj.name)
