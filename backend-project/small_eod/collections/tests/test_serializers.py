from django.test import TestCase

from ...generic.tests.test_serializers import ResourceSerializerMixin
from ..factories import CollectionFactory
from ..serializers import CollectionSerializer


class CollectionSerializerTestCase(ResourceSerializerMixin, TestCase):
    serializer_class = CollectionSerializer
    factory_class = CollectionFactory
