from test_plus.test import TestCase
from django.core import mail

from ...authkey.factories import KeyFactory
from ...generic.tests.test_views import GenericViewSetMixin, OrderingViewSetMixin
from ...search.tests.mixins import SearchQueryMixin
from ..factories import EventFactory
from ..serializers import EventSerializer


class EventViewSetTestCase(
    GenericViewSetMixin, OrderingViewSetMixin, SearchQueryMixin, TestCase
):
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

    def validate_notifications(self, action):
        mail_types = [_mail.extra_headers["Action"] for _mail in mail.outbox]
        self.assertEqual(mail_types, [action for _ in self.obj.case.notified_users.all()])

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

    def test_send_post_notifications(self):
        super().test_create_plain()
        self.assertGreater(len(mail.outbox), 0)
        self.validate_notifications("create")

    def test_send_delete_notifications(self):
        response = self.client.delete(
            self.get_url(name="detail", pk=self.obj.pk, **self.get_extra_kwargs()),
        )
        self.assertTrue(response.status_code, 200)
        self.assertGreater(len(mail.outbox), 0)
        self.validate_notifications("destroy")

    def test_send_patch_notifications(self):
        super().test_update_partial_plain()
        self.assertGreater(len(mail.outbox), 0)
        self.validate_notifications("partial_update")

    def test_notify_user_only_once(self):
        super().test_update_partial_plain()
        self.assertEqual(len(mail.outbox), len(self.obj.case.notified_users.all()))
