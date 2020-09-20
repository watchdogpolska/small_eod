from test_plus.test import TestCase

from ..serializers import FileSerializer
from ..factories import FileFactory
from ...generic.tests.test_views import GenericViewSetMixin


class FileViewSetTestCase(GenericViewSetMixin, TestCase):
    basename = "letter-file"
    serializer_class = FileSerializer
    factory_class = FileFactory

    def get_extra_kwargs(self):
        return {"letter_pk": self.obj.letter.pk}

    def validate_item(self, item):
        self.assertEqual(item["name"], self.obj.name)

    def increase_list(self):
        self.factory_class.create_batch(letter=self.obj.letter, size=5)
