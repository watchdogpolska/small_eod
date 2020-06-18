from django.core.management.base import BaseCommand

# from small_eod.administrative_units.factories
from small_eod.letters.factories import LetterFactory
from teryt_tree import models


class Command(BaseCommand):
    help = "Create initiala test data"

    def handle(self, *args, **options):
        LetterFactory.create_batch(size=10)
