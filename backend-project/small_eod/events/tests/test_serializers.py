from django.test import TestCase

from ...generic.tests.test_serializers import ResourceSerializerMixin
from ..factories import EventFactory
from ..serializers import EventSerializer


class EventSerializerTestCase(ResourceSerializerMixin, TestCase):
    serializer_class = EventSerializer
    factory_class = EventFactory
