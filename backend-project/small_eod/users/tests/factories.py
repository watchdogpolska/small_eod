from django.test import TestCase

from ..factories import UserFactory
from ..models import User
from ...generic.tests import FactoryCreateObjectsMixin


class UserFactoryTestCase(FactoryCreateObjectsMixin, TestCase):
    MODEL = User
    FACTORY = UserFactory
