from django.test import TestCase
from django.test import Client
from ..models import Event
from ...cases.models import Case
from django.utils import timezone
from django.urls import reverse
from ...authkey.models import Key, Scope
from django.contrib.auth import get_user_model


class EventIcalViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.case = Case.objects.create(name="case-title")
        self.event = Event.objects.create(
            date=timezone.now(), name="event-title", case=self.case
        )

    def test_refuse_for_unauthenticated(self):
        response = self.client.get(reverse("event-ical-list"))
        self.assertEqual(response.status_code, 403)

    def test_refuse_for_unauthorized(self):
        user = get_user_model().objects.create(username="user-1")
        key = Key.objects.create(user=user)
        response = self.client.get(
            path=reverse("event-ical-list"), data={"token": key.token}
        )

        self.assertEqual(response.status_code, 403)

    def test_accept_for_valid(self):
        user = get_user_model().objects.create(username="user-1")
        scope = Scope.objects.create(name="export_ical")
        key = Key.objects.create(user=user)
        key.scopes.set([scope])
        key.save()
        response = self.client.get(
            path=reverse("event-ical-list"), data={"token": key.token}
        )
        self.assertEqual(response.status_code, 200)
