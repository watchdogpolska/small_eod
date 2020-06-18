from io import StringIO

from django.test import TestCase
from django.core.management import call_command


class InitDataTestCase(TestCase):
    def test_success_two_run(self):
        stdout = StringIO()
        call_command(
            "init_data", stdout=stdout,
        )
        call_command(
            "init_data", stdout=stdout,
        )

    def test_create_letter(self):
        from ...letters.models import Letter

        stdout = StringIO()

        call_command(
            "init_data", stdout=stdout,
        )
        self.assertNotEqual(Letter.objects.count(), 0)
