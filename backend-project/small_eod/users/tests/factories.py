from django.test import TestCase

from ..factories import UserFactory
from ..models import User
from ...generic.tests.factories import FactoryTestCaseMixin


class UserFactoryTestCase(FactoryTestCaseMixin, TestCase):
    MODEL = User
    FACTORY = UserFactory
