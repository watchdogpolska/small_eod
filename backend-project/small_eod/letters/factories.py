import factory.fuzzy

from .models import Letter, DocumentType
from ..cases.factories import CaseFactory
from ..channels.factories import ChannelFactory
from ..generic.factories import (
    FuzzyTrueOrFalse,
    FuzzyDateTimeFromNow,
    AbstractTimestampUserFactory,
)
from ..institutions.factories import InstitutionFactory


class DocumentTypeFactory(factory.DjangoModelFactory):
    name = factory.Sequence(lambda n: "name-desscription-%04d" % n)

    class Meta:
        model = DocumentType


class LetterFactory(AbstractTimestampUserFactory, factory.DjangoModelFactory):

    final = FuzzyTrueOrFalse()
    date = FuzzyDateTimeFromNow(max_days=10)
    ordering = factory.fuzzy.FuzzyInteger(0, 100)
    direction = factory.fuzzy.FuzzyChoice(("IN", "OUT"))

    comment = factory.Sequence(lambda n: "letter-comment-%04d" % n)
    excerpt = factory.Sequence(lambda n: "letter-excerpt-%04d" % n)
    identifier = factory.Sequence(lambda n: "letter-identifier-%04d" % n)

    case = factory.SubFactory(CaseFactory)
    channel = factory.SubFactory(ChannelFactory)
    institution = factory.SubFactory(InstitutionFactory)
    document_type = factory.SubFactory(DocumentTypeFactory)

    class Meta:
        model = Letter
