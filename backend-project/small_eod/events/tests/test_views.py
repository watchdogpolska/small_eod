from test_plus.test import TestCase

from ..factories import EventFactory
from ..serializers import EventSerializer
from ...generic.tests.test_views import GenericViewSetMixin, OrderingViewSetMixin
from ...authkey.factories import KeyFactory


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

    def test_ical_failed_authenticate_to_via_session(self):
        self.login_required()
        response = self.client.get(
            self.get_url(name="ical", **self.get_extra_kwargs()),
        )
        self.assertEqual(response.status_code, 403)

    def get_with_key(self, *args, key, **kwargs):
        return self.client.get(
            *args, **kwargs, HTTP_AUTHORIZATION=f"Bearer {key.token}"
        )

    def test_ical_fail_authorization(self):
        key = KeyFactory(scopes=())
        response = self.get_with_key(
            path=self.get_url(name="ical", **self.get_extra_kwargs()), key=key
        )
        self.assertEqual(response.status_code, 403)

    def test_ical_validate_response_format(self):
        key = KeyFactory(scopes=("export_ical",))
        response = self.get_with_key(
            path=self.get_url(name="ical", **self.get_extra_kwargs()), key=key
        )
        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.get("Content-Type"), "text/calendar")
        body = response.content.decode("utf-8")
        self.assertIn(self.obj.name, body)
        self.assertIn(self.obj.comment, body)
        self.assertIn(self.obj.case.name, body)
