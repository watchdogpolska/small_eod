from io import StringIO

from django.test import TestCase
from django.core.management import call_command
from ...letters.models import Letter


class InitDataTestCase(TestCase):
    def test_success_two_run(self):
        stdout = StringIO()
        call_command(
            "init_data",
            "--minimum",
            stdout=stdout,
        )
        call_command(
            "init_data",
            "--minimum",
            stdout=stdout,
        )

    def test_create_letter(self):

        stdout = StringIO()

        call_command(
            "init_data",
            "--minimum",
            stdout=stdout,
        )
        self.assertNotEqual(Letter.objects.count(), 0)
