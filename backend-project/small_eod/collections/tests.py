from django.test import TestCase
from ..notes.factories import NoteFactory
from ..collections.factories import CollectionFactory
from django.urls import reverse
from ..generic.tests import ReadOnlyViewSetMixin
from ..users.factories import UserFactory

class NoteViewSetTestCase(ReadOnlyViewSetMixin, TestCase):
    basename = "collection-note"
    factory_class = NoteFactory
    def setUp(self):
        super().setUp()
        self.collection = CollectionFactory(query=str(self.obj.case.id))

    def get_extra_kwargs(self):
        return dict(collection_pk=self.collection.pk, case_pk=self.obj.case.pk)

    def validate_item(self, item):
        self.assertEqual(self.obj.comment, item["comment"])