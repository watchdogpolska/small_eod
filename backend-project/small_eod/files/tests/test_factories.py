from django.test import TestCase

from ...generic.tests.mixins import FactoryTestCaseMixin
from ..factories import FileFactory
from ..models import File


class FileFactoryTestCase(FactoryTestCaseMixin, TestCase):
    FACTORY = FileFactory
    MODEL = File
