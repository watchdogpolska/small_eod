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

    def test_render_as_ical(self):
        self.login_required()

        response = self.client.get(
            self.get_url(name="ical", **self.get_extra_kwargs()),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get("Content-Type"), "text/calendar")
        body = response.content.decode("utf-8")
        self.assertIn(self.obj.name, body)
        self.assertIn(self.obj.comment, body)
        self.assertIn(self.obj.case.name, body)
