from django.test import TestCase

from ..factories import UserFactory, UserWithCaseFactory
from ..models import User
from ...generic.tests.mixins import FactoryTestCaseMixin
from ...cases.factories import CaseFactory


class UserFactoryTestCase(FactoryTestCaseMixin, TestCase):
    MODEL = User
    FACTORY = UserFactory


class UserWithCaseFactoryTestCase(FactoryTestCaseMixin, TestCase):
    MODEL = User
    FACTORY = UserWithCaseFactory



