from test_plus.test import TestCase
from unittest.mock import patch
from ..factories import UserFactory
from ..serializers import UserSerializer
from ...generic.tests.test_views import ReadOnlyViewSetMixin, OrderingViewSetMixin


class UserViewSetTestCase(ReadOnlyViewSetMixin, OrderingViewSetMixin, TestCase):
    basename = "user"
    serializer_class = UserSerializer
    factory_class = UserFactory
    initial_count = 1
    ordering_fields = [
        "email",
        "email,-id",
    ]

    def validate_item(self, item):
        self.assertEqual(item["username"], self.obj.username)

    @patch(
        "small_eod.users.views.UserViewSet.provider",
        callback_url=lambda *args: ("redirect_url", "state"),
        exchange=lambda *args: {
            "email": "john@smith.com",
            "given_name": "John",
            "family_name": "Smith",
        },
    )
    def test_auth_success_flow(self, mock):
        auth_response = self.client.get(self.get_url(name="auth"))
        self.assertEqual(auth_response.status_code, 200)
        parsed_auth_response = auth_response.json()
        self.assertEqual(parsed_auth_response["url"], "redirect_url")

        code = "1234"
        exchange_response = self.client.get(
            self.get_url(name="exchange"), data={"code": code}
        )
        self.assertEqual(exchange_response.status_code, 200)
        parsed_exchange_response = exchange_response.json()

        refresh_token = parsed_exchange_response["refreshToken"]

        refresh_response = self.client.post(
            self.get_url(name="refresh"),
            data={"refreshToken": refresh_token},
            content_type="application/json",
        )
        self.assertEqual(refresh_response.status_code, 200)
        parsed_refresh_response = exchange_response.json()
        self.assertIn("accessToken", parsed_refresh_response)
        self.assertIn("refreshToken", parsed_refresh_response)
