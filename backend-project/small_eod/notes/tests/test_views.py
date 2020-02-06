from django.test import TestCase

from ..factories import NoteFactory
from ..serializers import NoteSerializer
from ...generic.tests.test_views import (
    GenericViewSetMixin,
    ReadOnlyViewSetMixin,
)


class NoteViewSetTestCase(GenericViewSetMixin, TestCase):
    basename = "note"
    serializer_class = NoteSerializer
    factory_class = NoteFactory

    def validate_item(self, item):
        self.assertEqual(item["comment"], self.obj.comment)
