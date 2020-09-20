from django.test import TestCase

from ...generic.tests.test_serializers import ResourceSerializerMixin
from ..factories import TagFactory
from ..serializers import TagSerializer


class TagSerializerTestCase(ResourceSerializerMixin, TestCase):
    serializer_class = TagSerializer
    factory_class = TagFactory
