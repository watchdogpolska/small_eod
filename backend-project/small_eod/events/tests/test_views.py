from django.test import TestCase

from ..factories import ChannelFactory
from ..serializers import ChannelSerializer
from ...generic.tests.test_views import (
    GenericViewSetMixin,
    ReadOnlyViewSetMixin,
)


class ChannelViewSetTestCase(GenericViewSetMixin, TestCase):
    basename = "channel"
    serializer_class = ChannelSerializer
    factory_class = ChannelFactory

    def validate_item(self, item):
        self.assertEqual(item["name"], self.obj.name)
