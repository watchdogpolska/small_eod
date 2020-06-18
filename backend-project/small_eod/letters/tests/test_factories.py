from django.test import TestCase

from ..factories import DocumentTypeFactory, LetterFactory
from ..models import DocumentType, Letter
from ...generic.tests.mixins import FactoryTestCaseMixin


class LetterFactoryTestCase(FactoryTestCaseMixin, TestCase):
    FACTORY = LetterFactory
    MODEL = Letter


class DocumentTypeFactoryTestCase(FactoryTestCaseMixin, TestCase):
    FACTORY = DocumentTypeFactory
    MODEL = DocumentType
