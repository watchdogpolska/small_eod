from django.test import TestCase

from ..factories import CollectionFactory
from ..serializers import CollectionSerializer
from ...generic.tests.test_views import ReadOnlyViewSetMixin, GenericViewSetMixin
from ...notes.factories import NoteFactory
from ...cases.factories import CaseFactory


class CollectionViewSetTestCase(GenericViewSetMixin, TestCase):

    basename = "collection"
    serializer_class = CollectionSerializer
    factory_class = CollectionFactory

    def validate_item(self, item):
        self.assertEqual(item["comment"], self.obj.comment)


class NoteViewSetTestCase(ReadOnlyViewSetMixin, TestCase):
    # todo move it to notes/tests.py?

    basename = "collection-note"
    factory_class = NoteFactory

    def setUp(self):
        super().setUp()
        self.collection = CollectionFactory(query=str(self.obj.case.id))

    def get_extra_kwargs(self):
        return dict(collection_pk=self.collection.pk, case_pk=self.obj.case.pk)

    def validate_item(self, item):
        self.assertEqual(self.obj.comment, item["comment"])


class CaseViewSetTestCase(ReadOnlyViewSetMixin, TestCase):

    basename = "collection-cases"
    factory_class = CaseFactory

    def setUp(self):
        super().setUp()
        self.collection = CollectionFactory(query=str(self.obj.id))

    def get_extra_kwargs(self):
        return dict(collection_pk=self.collection.pk)

    def validate_item(self, item):
        self.assertEqual(self.obj.name, item["name"])
