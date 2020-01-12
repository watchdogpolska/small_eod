from django.forms import model_to_dict
from django.test import TestCase

from .factories import AddressDataFactory, ExternalIdentifierFactory, InstitutionFactory
from .models import AddressData, ExternalIdentifier, Institution
from ..generic.tests import FactoryCreateObjectsMixin


class AddressDataFactoryTestCase(FactoryCreateObjectsMixin, TestCase):
    FACTORY = AddressDataFactory
    MODEL = AddressData

    def test_print_to_console(self):
        """
        Show in the console how the data looks like.
        Just making sure that frontend has the right data
        to work with.
        """
        print(f"\n{model_to_dict(self.FACTORY())}")


class ExternalIdentifierFactoryTestCase(FactoryCreateObjectsMixin, TestCase):
    FACTORY = ExternalIdentifierFactory
    MODEL = ExternalIdentifier


class InstitutionFactoryTestCase(FactoryCreateObjectsMixin, TestCase):
    FACTORY = InstitutionFactory
    MODEL = Institution
