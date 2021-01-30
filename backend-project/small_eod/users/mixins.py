from .factories import UserFactory


class AuthenticatedMixin:
    def login_required(self, is_staff=False, is_superuser=False):
        self.user = UserFactory(
            username="john", is_staff=is_staff, is_superuser=is_superuser
        )
        self.client.login(username="john", password="pass")
