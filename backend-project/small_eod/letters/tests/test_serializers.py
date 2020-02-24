from django.test import TestCase
from datetime import datetime, timedelta

from ..serializers import LetterSerializer, DescriptionSerializer

from ...generic.mixins import AuthRequiredMixin
from ..factories import LetterFactory, DescriptionFactory
from ...files.factories import FileFactory

# from ...channels.factories import ChannelFactory
from ...institutions.factories import InstitutionFactory
from ...cases.factories import CaseFactory


class DescriptionSerializerTestCase(TestCase):
    serializer_class = DescriptionSerializer
    factory_class = DescriptionFactory

    def setUp(self):
        self.obj = self.factory_class()

    def test_save(self):
        data = {"name": "Very important letter"}
        serializer = self.serializer_class(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        obj = serializer.save()
        self.assertEqual(obj.name, data["name"])

    def test_name_field(self):
        data = self.serializer_class(self.obj).data
        self.assertEqual(data["name"], self.obj.name)

    def test_update_name(self):
        serializer = self.serializer_class(
            self.obj, data={"name": "Not so important letter"}
        )
        self.assertTrue(serializer.is_valid(), serializer.errors)
        obj = serializer.save()
        self.assertEqual(serializer.data["name"], "Not so important letter")
        self.assertEqual(obj.name, "Not so important letter")


class LetterSerializerTestCase(AuthRequiredMixin, TestCase):
    serializer_class = LetterSerializer
    factory_class = LetterFactory

    def setUp(self):
        super().setUp()
        self.obj = self.factory_class()
        self.institution = InstitutionFactory()
        self.case = CaseFactory()

    def get_default_data(self, new_data=None, skip=None):
        new_data = new_data or {}
        skip = skip or []
        default_data = {
            "name": "Letter 1",
            "direction": "IN",
            "channel": {
                "name": "Semi Physical letter",
                "email": True,
                "city": True,
                "epuap": True,
                "house_no": True,
            },
            "final": True,
            "date": datetime.now() + timedelta(days=1),
            "identifier": "ssj2",
            "institution": self.institution.pk,
            "address": {
                "email": "test@test.test",
                "city": "Dzierżoniów",
                "epuap": "asdfg",
                "house_no": "666",
            },
            "case": self.case.pk,
            "ordering": 90,
            "comment": "comment",
            "excerpt": "No idea what this field does",
            "description": {"name": "A little important"},
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
        self.assertEqual(obj.name, "Letter 1")

    def test_fields(self):
        data = self.serializer_class(self.obj).data
        # self.assertEqual(
        # datetime.strptime(data["date"], "%Y-%m-%dT%H:%M:%S.%f%Z"),
        # self.obj.date) #TODO
        self.assertEqual(data["direction"], self.obj.direction)
        self.assertEqual(data["ordering"], self.obj.ordering)

    def test_nested_fields(self):
        data = self.serializer_class(self.obj).data
        self.assertEqual(data["address"]["email"], self.obj.address.email)
        self.assertEqual(data["address"]["city"], self.obj.address.city)
        self.assertEqual(data["channel"]["email"], self.obj.channel.email)
        self.assertEqual(data["description"]["name"], self.obj.description.name)

    def test_attachments(self):
        self.attachment = FileFactory(letter=self.obj)
        self.attachment2 = FileFactory(letter=self.obj)
        data = self.serializer_class(self.obj).data
        self.assertEqual(data["attachment"][0]["name"], self.attachment.name)
        self.assertEqual(data["attachment"][1]["name"], self.attachment2.name)
