from django.test import TestCase

from ..serializers import FileSerializer
from ..factories import FileFactory
from ...generic.tests.test_views import GenericViewSetMixin


class FileViewSetTestCase(GenericViewSetMixin, TestCase):
    basename = "letter-files"
    serializer_class = FileSerializer
    factory_class = FileFactory

    def get_extra_kwargs(self):
        return {"letter_pk": self.obj.letters.pk}

    def validate_item(self, item):
        self.assertEqual(item["name"], self.obj.name)
