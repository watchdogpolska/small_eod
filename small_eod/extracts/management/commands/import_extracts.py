import argparse
import csv
from django.db import transaction

from django.core.management.base import BaseCommand

from small_eod.extracts.models import Mail

FIELD_MAP = {
    'to': 'to_address',
    'from': 'from_address'
}


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('infile', nargs='+', type=argparse.FileType('r'))

    def handle(self, *args, **options):
        for file in options['infile']:
            c_file = csv.DictReader(file)
            with transaction.atomic():
                for row in c_file:
                    mapped = {FIELD_MAP.get(k, k): v for k, v in row.items()}
                    Mail.objects.create(**mapped)
