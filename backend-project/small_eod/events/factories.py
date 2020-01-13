import datetime

import factory.fuzzy
from django.utils import timezone

from .models import Event
from ..cases.factories import CaseFactory
from ..generic.factories import AbstractTimestampUserFactory


class EventFactory(AbstractTimestampUserFactory, factory.DjangoModelFactory):

    name = factory.Sequence(lambda n: "event-%04d" % n)
    case = factory.SubFactory(CaseFactory)
    comment = factory.Sequence(lambda n: "comment-event-%04d" % n)
    data = factory.fuzzy.FuzzyDateTime(
        start_dt=timezone.now(), end_dt=timezone.now() + datetime.timedelta(days=10),
    )

    class Meta:
        model = Event
