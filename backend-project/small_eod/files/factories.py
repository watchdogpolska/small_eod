import factory

from ..files.models import File
from ..letters.factories import LetterFactory


class FileFactory(factory.DjangoModelFactory):
    name = factory.Sequence(lambda n: f"file-{n:04}")
    path = factory.Sequence(lambda n: f"file-path-{n:04}")
    letter = factory.SubFactory(LetterFactory)

    class Meta:
        model = File
