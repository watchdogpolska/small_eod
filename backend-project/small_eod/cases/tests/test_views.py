from django.test import TestCase

from ..factories import CaseFactory
from ..serializers import CaseSerializer
from ...tags.factories import TagFactory
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

    def get_ommited_fields(self):
        return super().get_ommited_fields() + ["tags"]

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

    def test_create_with_tag(self):
        self.login_required()
        tags = [TagFactory().name]
        response = self.client.post(
            self.get_url(name="list", **self.get_extra_kwargs()),
            data=dict(tags=tags, ***self.get_create_data()),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201, response.json())
        item = response.json()
        self.assertCountEqual(item["tag"], tags)



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


class NotifiedUserViewSetTestCase(UserViewSetMixin, TestCase):
    user_type = "notified_users"
    basename = "case-notified_user"


class ResponsibleUserViewSetTestCase(UserViewSetMixin, TestCase):
    user_type = "responsible_users"
    basename = "case-responsible_user"
