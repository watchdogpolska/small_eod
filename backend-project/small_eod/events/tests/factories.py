from django.test import TestCase

from ..factories import EventFactory
from ..models import Event
from ...generic.tests import FactoryCreateObjectsMixin


class EventFactoryTestCase(FactoryCreateObjectsMixin, TestCase):
    FACTORY = EventFactory
    MODEL = Event
