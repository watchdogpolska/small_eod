from django.contrib.auth import get_user_model
from django.core import mail
from django.test import TestCase, override_settings
from django.utils import timezone

from .models import CaseEvent, EventType
from ..cases.models import Case, Person


@override_settings(
    EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend'
)
class EventTestCase(TestCase):

    def test_case_event(self):
        user_model = get_user_model()

        # create People
        users = [
            user_model(
                username='niceusername',
                email='niceusername@localhost',
            ),
            user_model(
                username='uglyusername',
                email='uglyusername@localhost',
            )
        ]; [u.save() for u in users]

        people = [
            Person(name=u.username, user=u)
            for u in users
        ]; [p.save() for p in people]

        # create Case
        case = Case(
            name='important case',
            comment='important comment',
        )
        case.save()
        [case.responsible_people.add(p) for p in people]
        case.save()

        # create Events
        event_type = EventType(
            name='case ends soon',
        ); event_type.save()

        event = CaseEvent(
            case=case,
            event_type=event_type,
            date=timezone.now(),
        ); event.save()

        # notify people about Event
        event.email_users()

        # verify
        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]
        [self.assertIn(u.email, email.to) for u in users]
        self.assertEqual(email.subject, 'case ends soon - important case')
        self.assertEqual(email.body, 'important case')
