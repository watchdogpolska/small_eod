from django.forms import modelform_factory
from django.test import TestCase

from .factories import AddressDataFactory, ExternalIdentifierFactory, InstitutionFactory
from .models import AddressData, ExternalIdentifier, Institution
from ..generic.tests import FactoryCreateObjectsMixin


class AddressDataFactoryTestCase(FactoryCreateObjectsMixin, TestCase):
    FACTORY = AddressDataFactory
    MODEL = AddressData


class ExternalIdentifierFactoryTestCase(FactoryCreateObjectsMixin, TestCase):
    FACTORY = ExternalIdentifierFactory
    MODEL = ExternalIdentifier


class InstitutionFactoryTestCase(FactoryCreateObjectsMixin, TestCase):
    FACTORY = InstitutionFactory
    MODEL = Institution


class AddressDataTestCase(TestCase):
    pass


class ExternalIdentifierTestCase(TestCase):
    pass


class InstituionTestCase(TestCase):
    pass


class ExternalIdentifierValidatorsTestCase(TestCase):
    """
    Test `validators` for model fields using `modelform_factory`.
    """

    def test_nip_accepts_digits(self):
        """
        `nip` accepts only digits.
        """
        f = modelform_factory(ExternalIdentifier, fields=('nip',))

        form = f(data=dict(nip='abc'))
        self.assertFalse(form.is_valid())

        form = f(data=dict(nip='9999999999'))
        self.assertTrue(form.is_valid())

    def test_nip_length(self):
        """
        `nip` accepts lenght of 10 only.
        """
        f = modelform_factory(ExternalIdentifier, fields=('nip',))

        chars_9 = '111111111'; self.assertEqual(len(chars_9), 9)
        chars_10 = '1111111111'; self.assertEqual(len(chars_10), 10)
        chars_11 = '11111111111'; self.assertEqual(len(chars_11), 11)

        form = f(data=dict(nip=chars_9))
        self.assertFalse(form.is_valid())

        form = f(data=dict(nip=chars_10))
        self.assertTrue(form.is_valid())

        form = f(data=dict(nip=chars_11))
        self.assertFalse(form.is_valid())

    def test_regon_accepts_digits(self):
        """
        `regon` accepts only digits.
        """
        f = modelform_factory(ExternalIdentifier, fields=('regon',))

        form = f(data=dict(regon='abc'))
        self.assertFalse(form.is_valid())

        form = f(data=dict(regon='9999999999'))
        self.assertTrue(form.is_valid())


    def test_regon_length(self):
        """
        `regon` accepts lenght of 10 or 14 only.
        """
        f = modelform_factory(ExternalIdentifier, fields=('regon',))

        chars_9 = '111111111'; self.assertEqual(len(chars_9), 9)
        chars_10 = '1111111111'; self.assertEqual(len(chars_10), 10)
        chars_11 = '11111111111'; self.assertEqual(len(chars_11), 11)
        chars_14 = '11111111111111'; self.assertEqual(len(chars_14), 14)

        form = f(data=dict(regon=chars_9))
        self.assertFalse(form.is_valid())

        form = f(data=dict(regon=chars_10))
        self.assertTrue(form.is_valid())

        form = f(data=dict(regon=chars_11))
        self.assertFalse(form.is_valid())

        form = f(data=dict(regon=chars_14))
        self.assertTrue(form.is_valid())
