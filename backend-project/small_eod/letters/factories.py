import factory.fuzzy

from .models import Letter, Description
from ..cases.factories import CaseFactory
from ..channels.factories import ChannelFactory
from ..generic.factories import (
    FuzzyTrueOrFalse,
    FuzzyDateTimeFromNow,
    AbstractTimestampUserFactory,
)
from ..institutions.factories import InstitutionFactory


class DescriptionFactory(factory.DjangoModelFactory):
    name = factory.Sequence(lambda n: "name-desscription-%04d" % n)

    class Meta:
        model = Description


class LetterFactory(AbstractTimestampUserFactory, factory.DjangoModelFactory):

    final = FuzzyTrueOrFalse()
    date = FuzzyDateTimeFromNow(max_days=10)
    ordering = factory.fuzzy.FuzzyInteger(0, 100)
    direction = factory.fuzzy.FuzzyChoice(("IN", "OUT"))

    name = factory.Sequence(lambda n: "letter-%04d" % n)
    comment = factory.Sequence(lambda n: "letter-comment-%04d" % n)
    excerpt = factory.Sequence(lambda n: "letter-excerpt-%04d" % n)
    identifier = factory.Sequence(lambda n: "letter-identifier-%04d" % n)

    case = factory.SubFactory(CaseFactory)
    channel = factory.SubFactory(ChannelFactory)
    institution = factory.SubFactory(InstitutionFactory)
    description = factory.SubFactory(DescriptionFactory)

    class Meta:
        model = Letter
