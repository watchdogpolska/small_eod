from django.test import TestCase

from ..factories import NoteFactory
from ..models import Note
from ...cases.models import Case
from ...generic.tests import FactoryCreateObjectsMixin


class NoteFactoryTestCase(FactoryCreateObjectsMixin, TestCase):
    FACTORY = NoteFactory
    MODEL = Note

    def test_foreign_keys(self):
        obj = self.create_factory()
        self.assertIsInstance(obj.case, Case)
