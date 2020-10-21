from django.test import TestCase

from ...generic.tests.test_serializers import ResourceSerializerMixin
from ..factories import NoteFactory
from ..serializers import NoteSerializer


class NoteSerializerTestCase(ResourceSerializerMixin, TestCase):
    serializer_class = NoteSerializer
    factory_class = NoteFactory
