import logging

from django.core.management.base import BaseCommand

from ...migrator import logger, run


class Command(BaseCommand):
    help = "Run Migrator"

    def add_arguments(self, parser):
        parser.add_argument(
            "--clean",
            action="store_true",
            help="Clean tables (use for testing, total cleanliness not guaranteed)",
        )

    def handle(self, clean, *args, **options):
        logger.setLevel(logging.DEBUG)
        run(clean=clean)
