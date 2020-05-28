from django.test import TestCase

from ..factories import InstitutionFactory
from ..models import Institution
from ...generic.tests.mixins import FactoryTestCaseMixin


class InstitutionFactoryTestCase(FactoryTestCaseMixin, TestCase):
    FACTORY = InstitutionFactory
    MODEL = Institution
