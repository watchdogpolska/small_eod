from django.test import TestCase

from ...generic.tests.test_serializers import ResourceSerializerMixin
from ..factories import ChannelFactory
from ..serializers import ChannelSerializer


class ChannelSerializerTestCase(ResourceSerializerMixin, TestCase):
    serializer_class = ChannelSerializer
    factory_class = ChannelFactory
