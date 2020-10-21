import factory.fuzzy
from factory.django import DjangoModelFactory
from ..generic.factories import AbstractTimestampUserFactory
from .models import Note
from ..cases.factories import CaseFactory


class NoteFactory(AbstractTimestampUserFactory, DjangoModelFactory):

    case = factory.SubFactory(CaseFactory)
    comment = factory.Sequence(lambda n: "comment-%04d" % n)

    class Meta:
        model = Note
