from test_plus.test import TestCase

from ..factories import CaseFactory
from ..serializers import CaseSerializer
from ...generic.tests.test_views import (
    GenericViewSetMixin,
    ReadOnlyViewSetMixin,
    AuthorshipViewSetMixin,
)
from ...users.factories import UserWithCaseFactory
from ...users.serializers import UserSerializer


class CaseViewSetTestCase(AuthorshipViewSetMixin, GenericViewSetMixin, TestCase):
    basename = "case"
    serializer_class = CaseSerializer
    factory_class = CaseFactory
    queries_less_than_limit = 15

    def validate_item(self, item):
        self.assertEqual(item["name"], self.obj.name)

    def test_create_minimum(self):
        self.login_required()
        name = "testowa-nazwa"
        response = self.client.post(
            self.get_url(name="list", **self.get_extra_kwargs()),
            data={"name": name},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201, response.json())
        item = response.json()
        self.assertEqual(item["name"], name)


class UserViewSetMixin(ReadOnlyViewSetMixin):
    user_type = None
    factory_class = UserWithCaseFactory
    serializer_class = UserSerializer
    queries_less_than_limit = 50

    def setUp(self):
        self.case = CaseFactory()
        super().setUp()

    def get_extra_kwargs(self):
        return dict(case_pk=self.case.pk)

    def get_extra_factory_kwargs(self):
        return {'hook__case': self.case}

    def validate_item(self, item):
        self.assertEqual(self.obj.username, item["username"])

    def test_list_no_users(self):
        self.login_required()
        field_dict = {self.__class__.user_type: []}
        self.case = CaseFactory(**field_dict)
        response = self.client.get(self.get_url(name="list", **self.get_extra_kwargs()))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(response.json().get(self.paginated_response_results_key)), 0
        )


class NotifiedUserViewSetTestCase(UserViewSetMixin, TestCase):
    user_type = "notified_users"
    basename = "case-notified_user"


class ResponsibleUserViewSetTestCase(UserViewSetMixin, TestCase):
    user_type = "responsible_users"
    basename = "case-responsible_user"
