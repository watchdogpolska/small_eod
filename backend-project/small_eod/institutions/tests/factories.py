from django.test import TestCase

from ..factories import (
    AddressDataFactory,
    ExternalIdentifierFactory,
    InstitutionFactory,
)
from ..models import AddressData, ExternalIdentifier, Institution
from ...generic.tests.factories import FactoryTestCaseMixin


class AddressDataFactoryTestCase(FactoryTestCaseMixin, TestCase):
    FACTORY = AddressDataFactory
    MODEL = AddressData


class ExternalIdentifierFactoryTestCase(FactoryTestCaseMixin, TestCase):
    FACTORY = ExternalIdentifierFactory
    MODEL = ExternalIdentifier


class InstitutionFactoryTestCase(FactoryTestCaseMixin, TestCase):
    FACTORY = InstitutionFactory
    MODEL = Institution
