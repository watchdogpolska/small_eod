from django.test import TestCase

from ..factories import DescriptionFactory, LetterFactory
from ..models import Description, Letter
from ...generic.tests import FactoryCreateObjectsMixin


class LetterFactoryTestCase(FactoryCreateObjectsMixin, TestCase):
    FACTORY = LetterFactory
    MODEL = Letter


class DescriptionFactoryTestCase(FactoryCreateObjectsMixin, TestCase):
    FACTORY = DescriptionFactory
    MODEL = Description
