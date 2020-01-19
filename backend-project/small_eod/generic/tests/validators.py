from django.core.validators import ValidationError
from django.test import TestCase

from ..validators import ExactLengthsValidator


class ExactLengthsValidatorTestCase(TestCase):
    def test_validator_message(self):
        """
        Validator returns corrrect error message.
        """
        validator = ExactLengthsValidator([10, 14, 566, 1])

        with self.assertRaises(ValidationError) as err:
            validator("12")

        self.assertIn(
            "Ensure this value has length of any [10, 14, 566, 1] (it has 2).",
            err.exception,
        )

    def test_validator_values(self):
        """
        Given invalid values, validator raises `ValidationError`.
        Given valid values, validator does not raise `ValidationError`.
        """
        validator = ExactLengthsValidator([10, 14])

        # valid values
        chars_10 = "1111111111"
        self.assertEqual(len(chars_10), 10)
        chars_14 = "11111111111111"
        self.assertEqual(len(chars_14), 14)

        # invalid values
        chars_9 = "111111111"
        self.assertEqual(len(chars_9), 9)
        chars_12 = "111111111111"
        self.assertEqual(len(chars_12), 12)
        chars_15 = "111111111111111"
        self.assertEqual(len(chars_15), 15)

        # valid test
        validator(chars_10)
        validator(chars_14)

        # invalid test
        with self.assertRaises(ValidationError):
            validator(chars_9)

        with self.assertRaises(ValidationError):
            validator(chars_12)

        with self.assertRaises(ValidationError):
            validator(chars_15)
