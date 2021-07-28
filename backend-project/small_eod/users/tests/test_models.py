from ..factories import UserFactory
from django.core import mail
from django.test import TestCase


class UserModelTestCase(TestCase):
    def test_send_enabled_mail_notification(self):
        kwargs = {"source": "NOTIFICATION", "action": "TEST"}
        user = UserFactory()
        user.notify(**kwargs)
        self.assertEqual(len(mail.outbox), 1)

    def test_do_not_send_disabled_notification(self):
        kwargs = {"source": "NOTIFICATION", "action": "DISABLED"}
        user = UserFactory()
        user.notify(**kwargs)
        self.assertEqual(len(mail.outbox), 0)

    def test_mail_notification_content_is_correct(self):
        kwargs = {"source": "NOTIFICATION", "action": "TEST", "username": "user"}
        user = UserFactory()
        user.notify(**kwargs)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "user wysłał testowe powiadomienie")
        self.assertEqual(mail.outbox[0].body, "testowe powiadomienie")
