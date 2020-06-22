from random import randint
from django.test import TestCase
import sys

from teryt_tree.factories import CategoryFactory
from ..factories import JednostkaAdministracyjnaFactory
from ..serializers import AdministrativeUnitSerializer
from ...generic.tests.test_views import GenericViewSetMixin


class CaseViewSetTestCase(GenericViewSetMixin, TestCase):
    basename = "administrative_unit"
    serializer_class = AdministrativeUnitSerializer
    factory_class = JednostkaAdministracyjnaFactory

    def get_int(self):
        return randint(10 ** 6, 10 ** 7 - 1)

    def get_create_data(self):
        return dict(id=self.get_int(), **super().get_create_data())

    def validate_item(self, item):
        self.assertEqual(item["name"], self.obj.name)

    def test_create_minimum(self):
        self.login_required()
        name = "testowa-nazwa"
        response = self.client.post(
            self.get_url(name="list", **self.get_extra_kwargs()),
            data={
                "id": self.get_int(),
                "name": name,
                "category": CategoryFactory().id,
                "updatedOn": "2020-06-23",
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201, response.json())
        item = response.json()
        self.assertEqual(item["name"], name)
