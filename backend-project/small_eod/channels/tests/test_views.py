from test_plus.test import TestCase

from ..factories import ChannelFactory
from ..serializers import ChannelSerializer
from ...generic.tests.test_views import GenericViewSetMixin


class ChannelViewSetTestCase(GenericViewSetMixin, TestCase):
    basename = "channel"
    serializer_class = ChannelSerializer
    factory_class = ChannelFactory
    queries_less_than_limit = 5

    def validate_item(self, item):
        self.assertEqual(item["name"], self.obj.name)
