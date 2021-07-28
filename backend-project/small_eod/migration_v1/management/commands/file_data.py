import json

from django.conf import settings
from django.core.management.base import BaseCommand

from ....files.models import File


class Command(BaseCommand):
    help = "Rudimentary command to get file path data for file migration"

    def add_arguments(self, parser):
        parser.add_argument(
            "--pretty",
            action="store_const",
            const=2,
            default=None,
            help="Print jsons with indent",
        )

    def handle(self, pretty, *args, **options):
        data = []
        for afile in File.objects.all():
            source = f"./{afile.name}"
            target = f"s3://{settings.MINIO_BUCKET}/{afile.path}"
            data.append([source, target])

        print(json.dumps(data, indent=pretty))
