from django.core.management.base import BaseCommand
import urllib.request
from django.core.management import call_command
from small_eod.letters.factories import LetterFactory
import tempfile

URL = (
    "http://cdn.files.jawne.info.pl/"
    + "public_html/2017/12/03_05_43_05/TERC_Urzedowy_2017-12-03.xml"
)


class Command(BaseCommand):
    help = "Create initial test data"

    def handle(self, *args, **options):
        with tempfile.NamedTemporaryFile() as fp:
            fp.write(urllib.request.urlopen(URL).read())
            call_command("load_terc", "--input", fp.name)

        LetterFactory.create_batch(size=10)
