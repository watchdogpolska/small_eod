import factory.fuzzy
from factory.django import DjangoModelFactory

from .models import Letter, DocumentType
from ..cases.factories import CaseFactory
from ..channels.factories import ChannelFactory
from ..generic.factories import (
    FuzzyTrueOrFalse,
    FuzzyDateTimeFromNow,
    AbstractTimestampUserFactory,
)
from ..institutions.factories import InstitutionFactory


class DocumentTypeFactory(DjangoModelFactory):
    name = factory.Sequence(lambda n: "name-desscription-%04d" % n)

    class Meta:
        model = DocumentType


class LetterFactory(AbstractTimestampUserFactory, DjangoModelFactory):

    final = FuzzyTrueOrFalse()
    date = FuzzyDateTimeFromNow(max_days=10)
    direction = factory.fuzzy.FuzzyChoice(("IN", "OUT"))

    comment = factory.Sequence(lambda n: "letter-comment-%04d" % n)
    excerpt = factory.Sequence(lambda n: "letter-excerpt-%04d" % n)
    reference_number = factory.Sequence(lambda n: "letter-reference_number-%04d" % n)

    case = factory.SubFactory(CaseFactory)
    channel = factory.SubFactory(ChannelFactory)
    institution = factory.SubFactory(InstitutionFactory)
    document_type = factory.SubFactory(DocumentTypeFactory)

    class Meta:
        model = Letter
