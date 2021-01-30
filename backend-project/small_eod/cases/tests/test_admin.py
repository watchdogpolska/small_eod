from django.test import TestCase
from django.urls import reverse
from ...users.mixins import AuthenticatedMixin
from ..models import Case


class TestAddAdminMixin:
    @property
    def model(self):
        raise NotImplementedError()

    def get_url(self):
        return reverse(
            f"admin:{self.model._meta.app_label}_{self.model._meta.model_name}_add"
        )


class TestCaseAddAdmin(TestAddAdminMixin, AuthenticatedMixin, TestCase):
    model = Case

    def test_should_display_form(self):
        self.login_reqired(is_staff=True, is_superuser=True)
        response = self.client.get(self.get_url(), follow=True)
        self.assertIn(
            f"<title>Add {self.model._meta.model_name} | Grappelli</title>",
            response.content.decode(),
        )
