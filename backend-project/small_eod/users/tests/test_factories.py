from django.test import TestCase

from ...generic.tests.mixins import FactoryTestCaseMixin
from ..factories import UserFactory
from ..models import User


class UserFactoryTestCase(FactoryTestCaseMixin, TestCase):
    MODEL = User
    FACTORY = UserFactory
