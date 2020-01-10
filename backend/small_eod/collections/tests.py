from django.test import TestCase
from ..notes.factories import NoteFactory
from ..collections.factories import CollectionFactory
from django.urls import reverse
from ..users.factories import UserFactory

class NoteViewSetTestCase(TestCase):
    basename = "collection-note"

    def setUp(self):
        self.note = NoteFactory()
        self.collection = CollectionFactory(query=str(self.note.case.id))
        self.user = getattr(self, "user", UserFactory(username="john"))
        self.client.login(username="john", password="pass")

    def get_url(self, name, **kwargs):
        return reverse("{}-{}".format(self.basename, name), kwargs=kwargs)

    def test_list_plain(self):
        response = self.client.get(
            self.get_url(name="list", collection_pk=self.collection.pk, case_pk=self.note.case.pk)
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_retrieve_plain(self):
        response = self.client.get(
            self.get_url(name="detail", collection_pk=self.collection.pk, case_pk=self.note.case.pk, pk=self.note.pk)
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["comment"], self.note.comment)