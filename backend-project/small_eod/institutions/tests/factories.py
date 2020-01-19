from django.test import TestCase

from ..factories import (
    AddressDataFactory,
    ExternalIdentifierFactory,
    InstitutionFactory,
)
from ..models import AddressData, ExternalIdentifier, Institution
from ...generic.tests import FactoryCreateObjectsMixin


class AddressDataFactoryTestCase(FactoryCreateObjectsMixin, TestCase):
    FACTORY = AddressDataFactory
    MODEL = AddressData


class ExternalIdentifierFactoryTestCase(FactoryCreateObjectsMixin, TestCase):
    FACTORY = ExternalIdentifierFactory
    MODEL = ExternalIdentifier


class InstitutionFactoryTestCase(FactoryCreateObjectsMixin, TestCase):
    FACTORY = InstitutionFactory
    MODEL = Institution
