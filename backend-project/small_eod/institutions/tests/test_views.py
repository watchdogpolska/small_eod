# TODO: Dodać test class InstitutionViewSetTestCase(AuthorshipViewSetMixin, TestCase).
# Atualnie taki test nie przechodzi z powodu problemów z factory (nieprawidłowe pk dla
#  AdministrativeUnit

from django.test import TestCase

from ..factories import InstitutionFactory
from ..serializers import InstitutionSerializer
from ...generic.tests.test_views import (
    GenericViewSetMixin,
    # ReadOnlyViewSetMixin,
    AuthorshipViewSetMixin,
)
# from ...users.factories import UserFactory
# from ...users.serializers import UserSerializer

class InstitutionViewSetTestCase(AuthorshipViewSetMixin, GenericViewSetMixin, TestCase):
    basename = "nstitution"
    serializer_class = InstitutionSerializer
    factory_class = InstitutionFactory

    def validate_item(self, item):
        self.assertEqual(item["name"], self.obj.name)