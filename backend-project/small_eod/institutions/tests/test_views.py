from django.test import TestCase

from ..factories import InstitutionFactory
from ..serializers import InstitutionSerializer
from ...generic.tests.test_views import (
    GenericViewSetMixin,
    AuthorshipViewSetMixin,
)
from parameterized import parameterized


class InstitutionViewSetTestCase(AuthorshipViewSetMixin, GenericViewSetMixin, TestCase):
    basename = "institution"
    serializer_class = InstitutionSerializer
    factory_class = InstitutionFactory

    def validate_item(self, item):
        self.assertEqual(item["name"], self.obj.name)

    @parameterized.expand(
        [
            ("CAT", ["CAT", "CATASTROPHE"]),
            ("cat", ["CAT", "CATASTROPHE"]),
            ("KITTY", ["KITTY"]),
            ("KIT", ["KITTY"]),
            ("INVALID", []),
        ]
    )
    def test_should_filter_by_name(self, query, expected_names):
        InstitutionFactory(name="KITTY")
        InstitutionFactory(name="CAT")
        InstitutionFactory(name="CATASTROPHE")

        self.login_required()
        response = self.client.get(
            self.get_url(name='list'),
            content_type="application/json",
            data={"query": query},
        )
        self.assertEqual(response.status_code, 200, response.json())
        names = [item["name"] for item in response.json()["results"]]
        self.assertEqual(expected_names, names)
