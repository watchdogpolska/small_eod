from test_plus.test import TestCase

from ..factories import CaseFactory
from ..serializers import CaseSerializer
from ...generic.tests.test_views import (
    GenericViewSetMixin,
    ReadOnlyViewSetMixin,
    AuthorshipViewSetMixin,
)
from ...users.factories import UserFactory
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
    factory_class = UserFactory
    serializer_class = UserSerializer

    def setUp(self):
        super().setUp()
        field_dict = {self.__class__.user_type: [self.obj.pk]}
        self.case = CaseFactory(**field_dict)

    def get_extra_kwargs(self):
        return dict(case_pk=self.case.pk)

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

    def test_num_queries_for_list(self):
        self.login_required()
        with self.assertNumQueriesLessThan(self.queries_less_than_limit):
            response = self.client.get(self.get_url_list())

        second_user = UserFactory()
        field_dict = {self.__class__.user_type: [self.obj.pk, second_user.pk]}
        self.case = CaseFactory(**field_dict)
        with self.assertNumQueriesLessThan(self.queries_less_than_limit):
            response = self.client.get(self.get_url_list())


class NotifiedUserViewSetTestCase(UserViewSetMixin, TestCase):
    user_type = "notified_users"
    basename = "case-notified_user"
    queries_less_than_limit = 6


class ResponsibleUserViewSetTestCase(UserViewSetMixin, TestCase):
    user_type = "responsible_users"
    basename = "case-responsible_user"
    queries_less_than_limit = 6
