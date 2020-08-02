from django.test import TestCase

from ..serializers import InstitutionSerializer
from ...generic.mixins import AuthRequiredMixin
from ...administrative_units.factories import AdministrativeUnitFactory
from ..factories import InstitutionFactory


class InstitutionSerializerTestCase(AuthRequiredMixin, TestCase):
    serializer_class = InstitutionSerializer
    factory_class = InstitutionFactory

    def setUp(self):
        super().setUp()
        self.admin_unit = AdministrativeUnitFactory(category__level=3)
        self.obj = self.factory_class()

    def get_default_data(self, new_data=None, skip=None):
        new_data = new_data or {}
        skip = skip or []
        default_data = {
            "name": "Polska Fundacja Narodowa",
            "administrative_unit": self.admin_unit.pk,
            "email": "test@test.test",
            "city": "Dzierżoniów",
            "epuap": "asdfg",
            "house_no": "666",
            "nip": "1234567890",
            "regon": "1234567890",
            "comment": "To są testowe dane",
            "tags": ["fundacje testowe"],
        }
        for field in skip:
            del default_data[field]
        return {
            **default_data,
            **new_data,
        }

    def test_save(self):
        self.login_required()
        serializer = self.serializer_class(
            data=self.get_default_data(), context={"request": self.request}
        )
        self.assertTrue(serializer.is_valid(), serializer.errors)
        obj = serializer.save()
        self.assertEqual(obj.name, "Polska Fundacja Narodowa")
        self.assertEqual(obj.comment, "To są testowe dane")
        tags = ["fundacje testowe"]
        for i, tag in enumerate(obj.tags.all()):
            self.assertEqual(tag.name, tags[i])

    def test_address_fields(self):
        data = self.serializer_class(self.obj).data
        self.assertEqual(data["house_no"], self.obj.house_no)
        self.assertEqual(data["city"], self.obj.city)

    def test_external_identifier_field(self):
        data = self.serializer_class(self.obj).data
        self.assertEqual(data["regon"], self.obj.regon)

    def test_comment_field(self):
        data = self.serializer_class(self.obj).data
        self.assertEqual(data["comment"], self.obj.comment)

    def test_tags_filed(self):
        data = self.serializer_class(self.obj).data
        for i, tag in enumerate(data["tags"]):
            self.assertEqual(tag, self.obj.tags.all()[i].name)

    def test_validate_administrative_unit(self):
        admin_unit = AdministrativeUnitFactory()
        serializer = self.serializer_class(
            data=self.get_default_data(new_data={"administrative_unit": admin_unit.pk}),
            context={"request": self.request},
        )
        self.assertFalse(serializer.is_valid(), serializer.errors)

    def test_update_name(self):
        self.login_required()
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

    def test_update_address(self):
        self.login_required()
        serializer = self.serializer_class(
            self.obj,
            data={"email": "new.email@asdf.pl"},
            context={"request": self.request},
            partial=True,
        )
        self.assertTrue(serializer.is_valid(), serializer.errors)
        obj = serializer.save()
        self.assertEqual(serializer.data["email"], "new.email@asdf.pl")
        self.assertEqual(obj.email, "new.email@asdf.pl")

    def test_update_nested_external_identifier(self):
        self.login_required()
        serializer = self.serializer_class(
            instance=self.obj,
            data={"nip": "1111111111"},
            context={"request": self.request},
            partial=True,
        )
        self.assertTrue(serializer.is_valid(), serializer.errors)
        obj = serializer.save()
        self.assertEqual(serializer.data["nip"], "1111111111")
        self.assertEqual(obj.nip, "1111111111")

    def test_update_comment(self):
        self.login_required()
        serializer = self.serializer_class(
            self.obj,
            data={"comment": "To jest nowy komentarz"},
            context={"request": self.request},
            partial=True,
        )
        self.assertTrue(serializer.is_valid(), serializer.errors)
        obj = serializer.save()
        self.assertEqual(serializer.data["comment"], "To jest nowy komentarz")
        self.assertEqual(obj.comment, "To jest nowy komentarz")

    def test_update_tags(self):
        self.login_required()
        serializer = self.serializer_class(
            self.obj,
            data={"tags": ["inne fundacje"]},
            context={"request": self.request},
            partial=True,
        )
        self.assertTrue(serializer.is_valid(), serializer.errors)
        obj = serializer.save()
        self.assertEqual(serializer.data["tags"], ["inne fundacje"])
        self.assertEqual(obj.tags.all()[0].name, "inne fundacje")
