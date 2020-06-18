from django.core.management.base import BaseCommand
from small_eod.letters.factories import LetterFactory

# from small_eod.administrative_units.factories
from teryt_tree.factories import JednostkaAdministracyjnaFactory
from teryt_tree import models


class JPKFactory(JednostkaAdministracyjnaFactory):
    class Meta:
        model = models.JednostkaAdministracyjna
        django_get_or_create = ("pk",)


class Command(BaseCommand):
    help = "Create initiala test data"

    def handle(self, *args, **options):
        JPKFactory.create_batch(size=10)
