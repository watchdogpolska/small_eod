from django.test import TestCase

from ..serializers import (
    InstitutionSerializer,
    ExternalIdentifierNestedSerializer,
    AddressDataNestedSerializer,
)
from ...generic.mixins import AuthRequiredMixin
from teryt_tree.factories import JednostkaAdministracyjnaFactory
from ..factories import (
    AddressDataFactory,
    ExternalIdentifierFactory,
    InstitutionFactory,
)


class AddressDataNestedSerializerTestCase(TestCase):
    serializer_class = AddressDataNestedSerializer
    factory_class = AddressDataFactory

    def setUp(self):
        self.obj = self.factory_class()

    def test_save(self):
        data = {"email": "asd@asd.pl"}
        serializer = self.serializer_class(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        obj = serializer.save()
        self.assertEqual(obj.email, data["email"])

    def test_data_fields(self):
        data = self.serializer_class(self.obj).data
        self.assertEqual(data["street"], self.obj.street)
        self.assertEqual(data["house_no"], self.obj.house_no)
        self.assertEqual(data["postal_code"], self.obj.postal_code)
        self.assertEqual(data["flat_no"], self.obj.flat_no)

    def test_update_city(self):
        serializer = self.serializer_class(self.obj, data={"city": "New City"})
        self.assertTrue(serializer.is_valid(), serializer.errors)
        obj = serializer.save()
        self.assertEqual(serializer.data["city"], "New City")
        self.assertEqual(obj.city, "New City")


class ExternalIdentifierSerializerTestCase(TestCase):
    serializer_class = ExternalIdentifierNestedSerializer
    factory_class = ExternalIdentifierFactory

    def setUp(self):
        self.obj = self.factory_class()

    def test_save(self):
        data = {"nip": "1234567890", "regon": "1234567890"}
        serializer = self.serializer_class(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        obj = serializer.save()
        self.assertEqual(obj.nip, data["nip"])
        self.assertEqual(obj.nip, data["regon"])

    def test_data_fields(self):
        data = self.serializer_class(self.obj).data
        self.assertTrue(data["nip"], self.obj.nip)

    def test_field_validation_inheritance(self):
        serializer = ExternalIdentifierNestedSerializer(
            data={"nip": "12345678901", "regon": "1234567890"}
        )
        self.assertFalse(serializer.is_valid(), serializer.errors)

    def test_update_nip(self):
        serializer = ExternalIdentifierNestedSerializer(
            instance=self.obj, data={"nip": "1111111111"}
        )
        self.assertTrue(serializer.is_valid(), serializer.errors)
        obj = serializer.save()
        self.assertEqual(serializer.data["nip"], "1111111111")
        self.assertEqual(obj.nip, "1111111111")


class InstitutionSerializerTestCase(AuthRequiredMixin, TestCase):
    serializer_class = InstitutionSerializer
    factory_class = InstitutionFactory

    def setUp(self):
        super().setUp()
        self.admin_unit = JednostkaAdministracyjnaFactory(category__level=3)
        self.obj = self.factory_class()

    def get_default_data(self, new_data=None, skip=None):
        new_data = new_data or {}
        skip = skip or []
        default_data = {
            "name": "Polska Fundacja Narodowa",
            "administrative_unit": self.admin_unit.pk,
            "address": {
                "email": "test@test.test",
                "city": "Dzierżoniów",
                "epuap": "asdfg",
                "house_no": "666",
            },
            "external_identifier": {"nip": "1234567890", "regon": "1234567890"},
        }
        for field in skip:
            del default_data[field]
        return {
            **default_data,
            **new_data,
        }

    def test_save(self):
        serializer = self.serializer_class(
            data=self.get_default_data(), context={"request": self.request}
        )
        self.assertTrue(serializer.is_valid(), serializer.errors)
        obj = serializer.save()
        self.assertEqual(obj.name, "Polska Fundacja Narodowa")

    def test_nested_address_fields(self):
        data = self.serializer_class(self.obj).data
        self.assertTrue(data["address"]["house_no"], self.obj.address.house_no)
        self.assertTrue(data["address"]["city"], self.obj.address.city)

    def test_data__external_identifier_field(self):
        data = self.serializer_class(self.obj).data
        self.assertTrue(
            data["external_identifier"]["regon"], self.obj.external_identifier.regon
        )

    def test_validate_administrative_unit(self):
        admin_unit = JednostkaAdministracyjnaFactory()
        serializer = self.serializer_class(
            data=self.get_default_data(new_data={"administrative_unit": admin_unit.pk}),
            context={"request": self.request},
        )
        self.assertFalse(serializer.is_valid(), serializer.errors)

    def test_update_name(self):
        serializer = self.serializer_class(
            self.obj,
            data={"name": "Inna nazwa sprawy"},
            context={"request": self.request},
            partial=True,
        )
        self.assertTrue(serializer.is_valid(), serializer.errors)
        obj = serializer.save()
        self.assertEqual(serializer.data["name"], "Inna nazwa sprawy")
        self.assertEqual(obj.name, "Inna nazwa sprawy")

    def test_update_nested_address(self):
        serializer = self.serializer_class(
            self.obj,
            data={"address": {"email": "new.email@asdf.pl"}},
            context={"request": self.request},
            partial=True,
        )
        self.assertTrue(serializer.is_valid(), serializer.errors)
        obj = serializer.save()
        self.assertEqual(serializer.data["address"]["email"], "new.email@asdf.pl")
        self.assertEqual(obj.address.email, "new.email@asdf.pl")

    def test_update_nested_external_identifier(self):
        serializer = self.serializer_class(
            instance=self.obj,
            data={"external_identifier": {"nip": "1111111111"}},
            context={"request": self.request},
            partial=True,
        )
        self.assertTrue(serializer.is_valid(), serializer.errors)
        obj = serializer.save()
        self.assertEqual(serializer.data["external_identifier"]["nip"], "1111111111")
        self.assertEqual(obj.external_identifier.nip, "1111111111")
