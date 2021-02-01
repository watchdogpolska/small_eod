from django.test import TestCase

from ...generic.tests.mixins import FactoryTestCaseMixin
from ..factories import InstitutionFactory
from ..models import Institution


class InstitutionFactoryTestCase(FactoryTestCaseMixin, TestCase):
    FACTORY = InstitutionFactory
    MODEL = Institution
