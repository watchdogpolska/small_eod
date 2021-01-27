from django.test import TestCase

from ...cases.models import Case
from ...generic.tests.mixins import FactoryTestCaseMixin
from ..factories import NoteFactory
from ..models import Note


class NoteFactoryTestCase(FactoryTestCaseMixin, TestCase):
    FACTORY = NoteFactory
    MODEL = Note

    def test_foreign_keys(self):
        obj = self.create_factory()
        self.assertIsInstance(obj.case, Case)
