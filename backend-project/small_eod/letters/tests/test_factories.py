from django.test import TestCase

from ...generic.tests.mixins import FactoryTestCaseMixin
from ..factories import DocumentTypeFactory, LetterFactory
from ..models import DocumentType, Letter


class LetterFactoryTestCase(FactoryTestCaseMixin, TestCase):
    FACTORY = LetterFactory
    MODEL = Letter


class DocumentTypeFactoryTestCase(FactoryTestCaseMixin, TestCase):
    FACTORY = DocumentTypeFactory
    MODEL = DocumentType
