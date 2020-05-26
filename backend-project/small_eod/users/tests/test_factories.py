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

    def test_magda(self):
        print("pomidorowa")
        case = CaseFactory()
        print(case.responsible_users.all())
        user = UserWithCaseFactory(hook__case=case)
        print(user)
        print(case.responsible_users.all())


