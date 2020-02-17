from django.test import TestCase

from ..models import File
from ..factories import FileFactory
from ...generic.tests.mixins import FactoryTestCaseMixin


class FileFactoryTestCase(FactoryTestCaseMixin, TestCase):
    FACTORY = FileFactory
    MODEL = File
