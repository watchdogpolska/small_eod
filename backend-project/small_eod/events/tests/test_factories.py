from django.test import TestCase

from ...generic.tests.mixins import FactoryTestCaseMixin
from ..factories import EventFactory
from ..models import Event


class EventFactoryTestCase(FactoryTestCaseMixin, TestCase):
    FACTORY = EventFactory
    MODEL = Event
