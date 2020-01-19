from django.test import TestCase

from .factories import NoteFactory
from .models import Note
from ..generic.tests import FactoryCreateObjectsMixin


class NoteFactoryTestCase(FactoryCreateObjectsMixin, TestCase):
    FACTORY = NoteFactory
    MODEL = Note
