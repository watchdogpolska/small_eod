from django.test import TestCase

from .factories import DictionaryFactory, FeatureFactory
from .models import Dictionary, Feature
from ..generic.tests import FactoryCreateObjectsMixin


class DictionaryFactoryTestCase(FactoryCreateObjectsMixin, TestCase):
    MODEL = Dictionary
    FACTORY = DictionaryFactory


class FeatureFactoryTestCase(FactoryCreateObjectsMixin, TestCase):
    MODEL = Feature
    FACTORY = FeatureFactory
