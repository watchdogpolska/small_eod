from django.test import TestCase

from ..factories import CollectionFactory
from ..serializers import CollectionSerializer
from ...generic.tests.test_views import (
    AuthorshipViewSetMixin,
    ReadOnlyViewSetMixin,
    GenericViewSetMixin
)
from ...notes.factories import NoteFactory
from ...cases.factories import CaseFactory
from ...cases.serializers import CaseSerializer


class CollectionViewSetTestCase(GenericViewSetMixin, TestCase):
    basename = "collection"
    serializer_class = CollectionSerializer
    factory_class = CollectionFactory

    def validate_item(self, item):
        self.assertEqual(item["comment"], self.obj.comment)


class CaseViewSetTestCase(AuthorshipViewSetMixin, GenericViewSetMixin, TestCase):
    basename = "collection-cases"
    serializer_class = CaseSerializer
    factory_class = CaseFactory

    def setUp(self):
        super().setUp()
        self.collection = CollectionFactory(query=str(self.obj.id))

    def get_extra_kwargs(self):
        return dict(collection_pk=self.collection.pk)

    def validate_item(self, item):
        self.assertEqual(item["name"], self.obj.name)


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
