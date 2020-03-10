from .factories import UserFactory


class AuthenticatedMixin:
    def login_required(self):
        self.user = UserFactory(username="john")
        self.client.login(username="john", password="pass")
