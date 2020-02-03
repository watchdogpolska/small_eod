from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate

from ..models import AddressData, ExternalIdentifier, Institution
from ..serializers import (
    InstitutionSerializer,
    ExternalIdentifierNestedSerializer,
    AddressDataNestedSerializer,
)
from ...users.factories import UserFactory
from teryt_tree.factories import JednostkaAdministracyjnaFactory, CategoryFactory


class AddressDataSerializerTestCase(TestCase):
    def setUp(self):
        self.default_serializer = AddressDataNestedSerializer(
            data={
                "email": "asd@asd.pl",
                "city": "City1",
                "epuap": "epuap",
                "street": "street",
                "house_no": "11",
                "postal_code": "22222",
                "flat_no": "",
            }
        )
        self.obj = (
            self.default_serializer.save()
            if self.default_serializer.is_valid()
            else None
        )

    def test_address_data_fields(self):
        self.assertEqual(self.obj.email, "asd@asd.pl")
        self.assertEqual(self.obj.city, "City1")
        self.assertEqual(self.obj.epuap, "epuap")
        data = AddressDataNestedSerializer(AddressData.objects.get()).data
        self.assertEqual(data["street"], "street")
        self.assertEqual(data["house_no"], "11")
        self.assertEqual(data["postal_code"], "22222")
        self.assertEqual(data["flat_no"], "")

    def test_update(self):
        serializer = AddressDataNestedSerializer(self.obj, data={"city": "New City"})
        self.assertTrue(serializer.is_valid(), serializer.errors)
        obj = serializer.save()
        self.assertEqual(serializer.data["city"], "New City")
        self.assertEqual(obj.city, "New City")


class ExternalIdentifierSerializerTestCase(TestCase):
    def setUp(self):
        self.default_serializer = ExternalIdentifierNestedSerializer(
            data={"nip": "1234567890", "regon": "1234567890"}
        )
        self.obj = (
            self.default_serializer.save()
            if self.default_serializer.is_valid()
            else None
        )

    def test_external_identifier_fields(self):
        self.assertEqual(self.obj.nip, "1234567890")
        data = ExternalIdentifierNestedSerializer(ExternalIdentifier.objects.get()).data
        self.assertTrue(data["regon"], "1234567890")

    def test_field_validation_inheritance(self):
        serializer = ExternalIdentifierNestedSerializer(
            data={"nip": "12345678901", "regon": "1234567890"}
        )
        self.assertFalse(serializer.is_valid(), serializer.errors)

    def test_update(self):
        serializer = ExternalIdentifierNestedSerializer(
            self.obj, data={"nip": "1111111111"}
        )
        self.assertTrue(serializer.is_valid(), serializer.errors)
        obj = serializer.save()
        self.assertEqual(serializer.data["nip"], "1111111111")
        self.assertEqual(obj.nip, "1111111111")


class InstitutionSerializerTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        factory = APIRequestFactory()
        self.request = factory.get("/")
        force_authenticate(self.request, user=self.user)
        self.request.user = self.user
        self.category = CategoryFactory(level=3)
        self.admin_unit = JednostkaAdministracyjnaFactory(category=self.category)
        self.default_serializer = InstitutionSerializer(
            data=self.get_default_data(), context={"request": self.request}
        )
        self.obj = (
            self.default_serializer.save()
            if self.default_serializer.is_valid()
            else None
        )

    def get_default_data(self, new_data=None, skip=None):
        new_data = new_data or {}
        skip = skip or []
        default_data = {
            "name": "Polska Fundacja Narodowa o rejestr umów",
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

    def test_nested_address_fields(self):
        self.assertEqual(self.obj.address.city, "Dzierżoniów")
        data = InstitutionSerializer(Institution.objects.get()).data
        self.assertTrue(data["address"]["house_no"], "666")

    def test_nested_external_identifier_fields(self):
        self.assertEqual(self.obj.external_identifier.nip, "1234567890")
        data = InstitutionSerializer(Institution.objects.get()).data
        self.assertTrue(data["external_identifier"]["regon"], "1234567890")

    def test_invalid_administrative_unit(self):
        admin_unit = JednostkaAdministracyjnaFactory()
        serializer = InstitutionSerializer(
            data=self.get_default_data(new_data={"administrative_unit": admin_unit.pk}),
            context={"request": self.request},
        )
        self.assertFalse(serializer.is_valid(), serializer.errors)

    def test_update(self):
        serializer = InstitutionSerializer(
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
        serializer = InstitutionSerializer(
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
        serializer = InstitutionSerializer(
            self.obj,
            data={"external_identifier": {"nip": "1111111111"}},
            context={"request": self.request},
            partial=True,
        )
        self.assertTrue(serializer.is_valid(), serializer.errors)
        obj = serializer.save()
        self.assertEqual(serializer.data["external_identifier"]["nip"], "1111111111")
        self.assertEqual(obj.external_identifier.nip, "1111111111")
