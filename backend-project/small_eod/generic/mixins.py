from ..users.factories import UserFactory
from rest_framework.test import APIRequestFactory, force_authenticate


class AuthRequiredMixin:
    def setUp(self):
        factory = APIRequestFactory()
        self.request = factory.get("/")

    def login_required(self):
        self.user = UserFactory()
        force_authenticate(self.request, user=self.user)
        self.request.user = self.user
