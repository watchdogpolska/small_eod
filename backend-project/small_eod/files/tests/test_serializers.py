from django.test import TestCase

from ...generic.tests.test_serializers import ResourceSerializerMixin
from ..factories import FileFactory
from ..serializers import FileSerializer


class FileSerializerTestCase(ResourceSerializerMixin, TestCase):
    serializer_class = FileSerializer
    factory_class = FileFactory
