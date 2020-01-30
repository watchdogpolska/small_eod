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
    def test_address_data_fields(self):
        serializer = AddressDataNestedSerializer(
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
        self.assertTrue(serializer.is_valid(), serializer.errors)
        obj = serializer.save()
        self.assertEqual(obj.email, "asd@asd.pl")
        self.assertEqual(obj.city, "City1")
        self.assertEqual(obj.epuap, "epuap")
        data = AddressDataNestedSerializer(AddressData.objects.get()).data
        self.assertEqual(data["street"], "street")
        self.assertEqual(data["house_no"], "11")
        self.assertEqual(data["postal_code"], "22222")
        self.assertEqual(data["flat_no"], "")


class ExternalIdentifierSerializerTestCase(TestCase):
    def test_external_identifier_fields(self):
        serializer = ExternalIdentifierNestedSerializer(
            data={"nip": "1234567890", "regon": "1234567890"}
        )
        self.assertTrue(serializer.is_valid(), serializer.errors)
        obj = serializer.save()
        self.assertEqual(obj.nip, "1234567890")
        data = ExternalIdentifierNestedSerializer(ExternalIdentifier.objects.get()).data
        self.assertTrue(data["regon"], "1234567890")

    def test_field_validation_inheritance(self):
        serializer = ExternalIdentifierNestedSerializer(
            data={"nip": "12345678901", "regon": "1234567890"}
        )
        self.assertFalse(serializer.is_valid(), serializer.errors)


class InstitutionSerializerTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        factory = APIRequestFactory()
        self.request = factory.get("/")
        force_authenticate(self.request, user=self.user)
        self.request.user = self.user
        self.category = CategoryFactory(level=3)
        self.admin_unit = JednostkaAdministracyjnaFactory(category=self.category)

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
        serializer = InstitutionSerializer(
            data=self.get_default_data(), context={"request": self.request}
        )
        self.assertTrue(serializer.is_valid(), serializer.errors)
        obj = serializer.save()
        self.assertEqual(obj.address.city, "Dzierżoniów")
        data = InstitutionSerializer(Institution.objects.get()).data
        self.assertTrue(data["address"]["house_no"], "666")

    def test_nested_external_identifier_fields(self):
        serializer = InstitutionSerializer(
            data=self.get_default_data(), context={"request": self.request}
        )
        self.assertTrue(serializer.is_valid(), serializer.errors)
        obj = serializer.save()
        self.assertEqual(obj.external_identifier.nip, "1234567890")
        data = InstitutionSerializer(Institution.objects.get()).data
        self.assertTrue(data["external_identifier"]["regon"], "1234567890")

    def test_invalid_administrative_unit(self):
        admin_unit = JednostkaAdministracyjnaFactory()
        serializer = InstitutionSerializer(
            data=self.get_default_data(new_data={"administrative_unit": admin_unit.pk}),
            context={"request": self.request},
        )
        self.assertFalse(serializer.is_valid(), serializer.errors)
