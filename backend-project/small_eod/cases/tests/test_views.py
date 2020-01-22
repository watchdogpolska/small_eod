from django.test import TestCase

from ..factories import CaseFactory
from ..serializers import CaseSerializer
from ...generic.tests.test_views import (
    GenericViewSetMixin,
    ReadOnlyViewSetMixin,
)
from ...users.factories import UserFactory
from ...users.serializers import UserSerializer


class CaseViewSetTestCase(GenericViewSetMixin, TestCase):
    basename = "case"
    serializer_class = CaseSerializer
    factory_class = CaseFactory

    def validate_item(self, item):
        self.assertEqual(item["name"], self.obj.name)


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
        field_dict = {self.__class__.user_type: []}
        self.case = CaseFactory(**field_dict)
        response = self.client.get(self.get_url(name="list", **self.get_extra_kwargs()))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 0)


class NotifiedUserViewSetTestCase(UserViewSetMixin, TestCase):
    user_type = "notified_users"
    basename = "case-notified_user"


class ResponsibleUserViewSetTestCase(UserViewSetMixin, TestCase):
    user_type = "responsible_users"
    basename = "case-responsible_user"
