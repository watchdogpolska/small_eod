from django.forms import modelform_factory
from django.test import TestCase

from ..models import Institution
from ...administrative_units.factories import AdministrativeUnitFactory


class ExternalIdentifierValidatorsTestCase(TestCase):
    """
    Test `validators` for model fields using `modelform_factory`.
    """

    def test_nip_accepts_digits(self):
        """
        `nip` accepts only digits.
        """
        f = modelform_factory(Institution, fields=("nip",))

        form = f(data=dict(nip="abc"))
        self.assertFalse(form.is_valid())

        form = f(data=dict(nip="9999999999"))
        self.assertTrue(form.is_valid())

        form = f(data=dict(nip="abc1234567"))
        self.assertFalse(form.is_valid())

    def test_nip_length(self):
        """
        `nip` accepts length of 10 only.
        """
        f = modelform_factory(Institution, fields=("nip",))

        chars_9 = "111111111"
        self.assertEqual(len(chars_9), 9)
        chars_10 = "1111111111"
        self.assertEqual(len(chars_10), 10)
        chars_11 = "11111111111"
        self.assertEqual(len(chars_11), 11)

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
        f = modelform_factory(Institution, fields=("regon",))

        form = f(data=dict(regon="abc"))
        self.assertFalse(form.is_valid())

        form = f(data=dict(regon="9999999999"))
        self.assertTrue(form.is_valid())

        form = f(data=dict(regon="abc1234567"))
        self.assertFalse(form.is_valid())

    def test_regon_length(self):
        """
        `regon` accepts length of 10 or 14 only.
        """
        f = modelform_factory(Institution, fields=("regon",))

        chars_9 = "111111111"
        self.assertEqual(len(chars_9), 9)
        chars_10 = "1111111111"
        self.assertEqual(len(chars_10), 10)
        chars_11 = "11111111111"
        self.assertEqual(len(chars_11), 11)
        chars_14 = "11111111111111"
        self.assertEqual(len(chars_14), 14)

        form = f(data=dict(regon=chars_9))
        self.assertFalse(form.is_valid())

        form = f(data=dict(regon=chars_10))
        self.assertTrue(form.is_valid())

        form = f(data=dict(regon=chars_11))
        self.assertFalse(form.is_valid())

        form = f(data=dict(regon=chars_14))
        self.assertTrue(form.is_valid())


class InstitutionValidatorsTestCase(TestCase):
    def test_level_3_positive(self):
        """
        Administrative unit must be a level 3 unit.
        """
        f = modelform_factory(Institution, fields=("administrative_unit",))

        administrative_unit = AdministrativeUnitFactory(category__level=3)
        self.assertEqual(administrative_unit.category.level, 3)
        form = f(data=dict(administrative_unit=administrative_unit.pk))
        self.assertTrue(form.is_valid())

    def test_level_3_negative(self):
        f = modelform_factory(Institution, fields=("administrative_unit",))

        administrative_unit = AdministrativeUnitFactory(category__level=1)
        self.assertEqual(administrative_unit.category.level, 1)
        form = f(data=dict(administrative_unit=administrative_unit.pk))
        self.assertFalse(form.is_valid())
