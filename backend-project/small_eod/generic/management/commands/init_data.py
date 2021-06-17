import tempfile
import urllib.request

from django.core.management import call_command
from django.core.management.base import BaseCommand

from ....letters.factories import LetterFactory
from ....events.factories import EventFactory
from ....notes.factories import NoteFactory

URL = (
    "http://cdn.files.jawne.info.pl/"
    + "public_html/2017/12/03_05_43_05/TERC_Urzedowy_2017-12-03.xml"
)


class Command(BaseCommand):
    help = "Create initial test data"

    def add_arguments(self, parser):
        parser.add_argument(
            "--minimum",
            action="store_true",
            help="Use minimum set of data",
        )

    def handle(self, minimum, *args, **options):
        with tempfile.NamedTemporaryFile() as fp:
            fp.write(urllib.request.urlopen(URL).read())
            args = ["--input", fp.name]
            if minimum:
                args = args + ["--limit", 50]
            call_command("load_terc", *args, stdout=self.stdout)

        # Letter factory creates dependencies recursively.
        # As a result, all related tables, not just Letters, are filled with some data.
        LetterFactory.create_batch(size=10)

        # Create a few objects not created by the LetterFactory.
        EventFactory.create_batch(size=5)
        NoteFactory.create_batch(size=5)
