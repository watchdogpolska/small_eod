from django.test import TestCase

from .factories import CollectionFactory
from .models import Collection
from ..generic.tests import ReadOnlyViewSetMixin, FactoryCreateObjectsMixin
from ..notes.factories import NoteFactory


class CollectionFactoryTestCase(FactoryCreateObjectsMixin, TestCase):
    FACTORY = CollectionFactory
    MODEL = Collection


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
