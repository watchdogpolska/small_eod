from ..users.factories import UserFactory
from rest_framework.test import APIRequestFactory, force_authenticate


class AuthRequiredMixin:
    def setUp(self):
        self.user = UserFactory()
        factory = APIRequestFactory()
        self.request = factory.get("/")
        force_authenticate(self.request, user=self.user)
        self.request.user = self.user
