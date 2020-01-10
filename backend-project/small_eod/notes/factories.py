import factory
import factory.fuzzy
from django.utils import timezone
import datetime
from .models import Note
from ..cases.factories import CaseFactory


class NoteFactory(factory.django.DjangoModelFactory):
    case = factory.SubFactory(CaseFactory)
    comment = factory.Sequence(lambda n: "comment-%04d" % n)

    class Meta:
        model = Note
