from django.forms import modelform_factory
from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate

from ..factories import AddressDataFactory, ExternalIdentifierFactory, InstitutionFactory
from ..models import AddressData, ExternalIdentifier, Institution
from ..serializers import (
    InstitutionSerializer,
    AddressDataNestedSerializer,
    ExternalIdentifierNestedSerializer,
)
from ...users.factories import UserFactory
from teryt_tree.factories import JednostkaAdministracyjnaFactory, CategoryFactory


class AddressDataTestCase(TestCase):
    pass


class ExternalIdentifierTestCase(TestCase):
    pass


class InstitutionTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        factory = APIRequestFactory()
        self.request = factory.get("/")
        force_authenticate(self.request, user=self.user)
        self.request.user = self.user
        self.admin_unit = JednostkaAdministracyjnaFactory()

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
            "external_identifier": {"nip": "123456789", "regon": "1234567890",},
        }
        for field in skip:
            del default_data[field]
        return {
            **default_data,
            **new_data,
        }

    def test_address_fields(self):
        serializer = InstitutionSerializer(
            data=self.get_default_data(), context={"request": self.request}
        )
        self.assertTrue(serializer.is_valid(), serializer.errors)
        obj = serializer.save()
        self.assertTrue(AddressData.objects.count(), 1)
        self.assertEqual(obj.address.city, "Dzierżoniów")
        data = InstitutionSerializer(Institution.objects.get()).data
        self.assertTrue(data["address"]["house_no"], "666")

    def test_related_address_data(self):
        pass


class ExternalIdentifierValidatorsTestCase(TestCase):
    """
    Test `validators` for model fields using `modelform_factory`.
    """

    def test_nip_accepts_digits(self):
        """
        `nip` accepts only digits.
        """
        f = modelform_factory(ExternalIdentifier, fields=("nip",))

        form = f(data=dict(nip="abc"))
        self.assertFalse(form.is_valid())

        form = f(data=dict(nip="9999999999"))
        self.assertTrue(form.is_valid())

        form = f(data=dict(nip="abc1234567"))
        self.assertFalse(form.is_valid())

    def test_nip_length(self):
        """
        `nip` accepts length of 10 only.
        """
        f = modelform_factory(ExternalIdentifier, fields=("nip",))

        chars_9 = "111111111"
        self.assertEqual(len(chars_9), 9)
        chars_10 = "1111111111"
        self.assertEqual(len(chars_10), 10)
        chars_11 = "11111111111"
        self.assertEqual(len(chars_11), 11)

        form = f(data=dict(nip=chars_9))
        self.assertFalse(form.is_valid())

        form = f(data=dict(nip=chars_10))
        self.assertTrue(form.is_valid())

        form = f(data=dict(nip=chars_11))
        self.assertFalse(form.is_valid())

    def test_regon_accepts_digits(self):
        """
        `regon` accepts only digits.
        """
        f = modelform_factory(ExternalIdentifier, fields=("regon",))

        form = f(data=dict(regon="abc"))
        self.assertFalse(form.is_valid())

        form = f(data=dict(regon="9999999999"))
        self.assertTrue(form.is_valid())

        form = f(data=dict(regon="abc1234567"))
        self.assertFalse(form.is_valid())

    def test_regon_length(self):
        """
        `regon` accepts length of 10 or 14 only.
        """
        f = modelform_factory(ExternalIdentifier, fields=("regon",))

        chars_9 = "111111111"
        self.assertEqual(len(chars_9), 9)
        chars_10 = "1111111111"
        self.assertEqual(len(chars_10), 10)
        chars_11 = "11111111111"
        self.assertEqual(len(chars_11), 11)
        chars_14 = "11111111111111"
        self.assertEqual(len(chars_14), 14)

        form = f(data=dict(regon=chars_9))
        self.assertFalse(form.is_valid())

        form = f(data=dict(regon=chars_10))
        self.assertTrue(form.is_valid())

        form = f(data=dict(regon=chars_11))
        self.assertFalse(form.is_valid())

        form = f(data=dict(regon=chars_14))
        self.assertTrue(form.is_valid())


class InstitutionValidatorsTestCase(TestCase):
    def test_level_3(self):
        """
        Administrative unit must be a level 3 unit.
        """
        category1 = CategoryFactory(level=1)
        administrative_unit = JednostkaAdministracyjnaFactory(category=category1)

        f = modelform_factory(Institution, fields=("administrative_unit",))

        self.assertEqual(administrative_unit.category.level, 1)
        form = f(data=dict(administrative_unit=administrative_unit))
        self.assertFalse(form.is_valid())

        category3 = CategoryFactory(level=3)
        administrative_unit = JednostkaAdministracyjnaFactory(category=category3)
        self.assertEqual(administrative_unit.category.level, 3)
        form = f(data=dict(administrative_unit=administrative_unit))
        self.assertTrue(form.is_valid())
