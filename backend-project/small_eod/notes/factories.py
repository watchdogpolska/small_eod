import factory.fuzzy
from ..generic.factories import AbstractTimestampUserFactory
from .models import Note
from ..cases.factories import CaseFactory


class NoteFactory(AbstractTimestampUserFactory, factory.DjangoModelFactory):

    case = factory.SubFactory(CaseFactory)
    comment = factory.Sequence(lambda n: "comment-%04d" % n)

    class Meta:
        model = Note
        django_get_or_create = ("pk",)
