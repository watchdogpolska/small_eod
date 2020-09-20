from test_plus.test import TestCase

from ..factories import EventFactory
from ..serializers import EventSerializer
from ...generic.tests.test_views import GenericViewSetMixin, OrderingViewSetMixin


class EventViewSetTestCase(GenericViewSetMixin, OrderingViewSetMixin, TestCase):
    basename = "event"
    serializer_class = EventSerializer
    factory_class = EventFactory
    ordering_fields = [
        "case__name",
        "-name",
        "-date,comment",
    ]

    def validate_item(self, item):
        self.assertEqual(item["name"], self.obj.name)
