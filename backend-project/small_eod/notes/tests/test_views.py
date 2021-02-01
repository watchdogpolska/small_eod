from test_plus.test import TestCase

from ...generic.tests.test_views import GenericViewSetMixin, OrderingViewSetMixin
from ..factories import NoteFactory
from ..serializers import NoteSerializer

from ...search.tests.mixins import SearchQueryMixin


class NoteViewSetTestCase(
    GenericViewSetMixin, OrderingViewSetMixin, SearchQueryMixin, TestCase
):
    basename = "note"
    serializer_class = NoteSerializer
    factory_class = NoteFactory
    ordering_fields = [
        "case__name",
    ]

    def validate_item(self, item):
        self.assertEqual(item["comment"], self.obj.comment)

    def get_update_data(self):
        return {"comment": f"{self.obj.comment}-updated"}

    def validate_update_item(self, item):
        self.assertEqual(item["id"], self.obj.pk)
        self.assertEqual(item["comment"], f"{self.obj.comment}-updated")
