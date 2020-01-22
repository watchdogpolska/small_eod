from django.test import TestCase

from ..factories import DescriptionFactory, LetterFactory
from ..models import Description, Letter
from ...generic.tests.mixins import FactoryTestCaseMixin


class LetterFactoryTestCase(FactoryTestCaseMixin, TestCase):
    FACTORY = LetterFactory
    MODEL = Letter


class DescriptionFactoryTestCase(FactoryTestCaseMixin, TestCase):
    FACTORY = DescriptionFactory
    MODEL = Description
