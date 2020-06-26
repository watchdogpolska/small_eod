from django.test import TestCase
from django.urls import reverse
from ...users.mixins import AuthenticatedMixin


class TestAddAdminMixin:
    @property
    def app_label(self):
        raise NotImplementedError()

    @property
    def model_name(self):
        raise NotImplementedError()

    def get_url(self):
        return reverse(f"admin:{self.app_label}_{self.model_name}_add")


class TestCaseAddAdmin(TestAddAdminMixin, AuthenticatedMixin, TestCase):
    app_label = "cases"
    model_name = "case"

    def test_should_display_form(self):
        self.login_required(is_staff=True, is_superuser=True)
        response = self.client.get(self.get_url(), follow=True)
        self.assertIn(
            f"<title>Add {self.model_name} | Grappelli</title>",
            response.content.decode(),
        )
