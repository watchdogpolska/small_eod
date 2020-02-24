from django.test import TestCase

from ..serializers import LetterSerializer, DescriptionSerializer

from ...generic.mixins import AuthRequiredMixin
from ..factories import LetterFactory, DescriptionFactory


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
        self.obj = self.factory_class()
