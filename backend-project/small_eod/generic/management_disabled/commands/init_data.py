from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Create initial test data"

    def handle(self, *args, **options):
        from small_eod.letters.factories import LetterFactory
        LetterFactory.create_batch(size=10)
