from django.test import TestCase
from django.utils.timezone import datetime, timedelta

from ..serializers import LetterSerializer, DocumentTypeSerializer

from ...generic.mixins import AuthRequiredMixin
from ...generic.tests.test_serializers import ResourceSerializerMixin
from ..factories import LetterFactory, DocumentTypeFactory
from ...files.factories import FileFactory
from ...channels.factories import ChannelFactory

# from ...channels.factories import ChannelFactory
from ...institutions.factories import InstitutionFactory
from ...cases.factories import CaseFactory


class DocumentTypeSerializerTestCase(ResourceSerializerMixin, TestCase):
    serializer_class = DocumentTypeSerializer
    factory_class = DocumentTypeFactory

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


class LetterSerializerTestCase(ResourceSerializerMixin, AuthRequiredMixin, TestCase):
    serializer_class = LetterSerializer
    factory_class = LetterFactory

    def setUp(self):
        super().setUp()
        self.obj = self.factory_class()
        self.institution = InstitutionFactory()
        self.case = CaseFactory()
        self.channel = ChannelFactory()
        self.document_type = DocumentTypeFactory()

    def get_default_data(self, new_data=None, skip=None):
        new_data = new_data or {}
        skip = skip or []
        default_data = {
            "direction": "IN",
            "channel": self.channel.pk,
            "final": True,
            "date": datetime.now() + timedelta(days=1),
            "reference_number": "ssj2",
            "institution": self.institution.pk,
            "case": self.case.pk,
            "ordering": 90,
            "comment": "comment",
            "excerpt": "No idea what this field does",
            "document_type": self.document_type.pk,
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
        self.assertEqual(obj.comment, "comment")

    def test_save_minimum(self):
        self.login_required()
        serializer = self.serializer_class(
            data={"comment": "comment"}, context={"request": self.request}
        )
        self.assertTrue(serializer.is_valid(), serializer.errors)
        obj = serializer.save()
        self.assertEqual(obj.comment, "comment")

    def test_fields(self):
        data = self.serializer_class(self.obj).data
        # self.assertEqual(
        # datetime.strptime(data["date"], "%Y-%m-%dT%H:%M:%S.%f%Z"),
        # self.obj.date) #TODO
        self.assertEqual(data["direction"], self.obj.direction)
        self.assertEqual(data["ordering"], self.obj.ordering)

    def test_nested_fields(self):
        data = self.serializer_class(self.obj).data
        self.assertEqual(data["document_type"], self.obj.document_type.pk)

    def test_attachments(self):
        self.attachment = FileFactory(letter=self.obj)
        self.attachment2 = FileFactory(letter=self.obj)
        data = self.serializer_class(self.obj).data
        self.assertEqual(data["attachments"][0]["name"], self.attachment.name)
        self.assertEqual(data["attachments"][1]["name"], self.attachment2.name)
