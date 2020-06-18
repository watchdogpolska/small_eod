import os
import time
import struct
import random
from unittest import skipIf
from io import StringIO

from django.test import TestCase
from django.core.management import call_command


class InitDataTestCase(TestCase):
    def test_success_two_rn(self):
        stdout = StringIO()
        call_command(
            "init_data", stdout=stdout,
        )
        call_command(
            "init_data", stdout=stdout,
        )

    def test_create_letter(self):
        from small_eod.letters.models import Letter
        stdout = StringIO()

        call_command(
            "init_data", stdout=stdout,
        )
        self.assertNotEqual(Letter.objects.count(), 0)
