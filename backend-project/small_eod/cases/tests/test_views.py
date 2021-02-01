from test_plus.test import TestCase

from ...generic.tests.test_views import (
    AuthorshipViewSetMixin,
    GenericViewSetMixin,
    OrderingViewSetMixin,
    ReadOnlyViewSetMixin,
    RelatedM2MMixin,
)
from ...tags.factories import TagFactory
from ...users.factories import UserFactory
from ...users.serializers import UserSerializer
from ..factories import CaseFactory
from ..serializers import CaseSerializer


class CaseViewSetTestCase(
    AuthorshipViewSetMixin, GenericViewSetMixin, OrderingViewSetMixin, TestCase
):
    basename = "case"
    serializer_class = CaseSerializer
    factory_class = CaseFactory
    ordering_fields = [
        "comment",
        "-comment",
        "created_on",
        "created_by__username",
        "-created_by__username,comment",
    ]

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

    def test_update_with_tag(self):
        self.login_required()
        tags = [TagFactory().name]
        response = self.client.put(
            self.get_url(name="detail", **self.get_extra_kwargs(), pk=self.obj.pk),
            data={**self.get_create_data(), "tags": tags},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200, response.json())
        item = response.json()
        self.assertCountEqual(item["tags"], tags)

    def test_search_by_pk(self):
        self.login_required()
        second_case = CaseFactory()
        response = self.client.get(
            self.get_url(name="list", **self.get_extra_kwargs()),
            data={"query": f"id:{second_case.pk}"},
        )
        self.assertEqual(response.status_code, 200, response.json())
        item = response.json()["results"]
        self.assertEqual(len(item), 1)
        self.assertEqual(item[0]["id"], second_case.pk)

    def test_search_invalid(self):
        self.login_required()
        response = self.client.get(
            self.get_url(name="list", **self.get_extra_kwargs()),
            data={"query": "id:"},
        )
        self.assertEqual(response.status_code, 400, response.json())
        item = response.json()
        self.assertEqual(
            item["query"][0],
            "Expected end of text, found ':'  (at char 2), (line:1, col:3)",
        )


class UserViewSetMixin(RelatedM2MMixin, ReadOnlyViewSetMixin):
    factory_class = UserFactory
    serializer_class = UserSerializer
    parent_factory_class = CaseFactory
    ordering_fields = [
        "-email",
        "email,-id",
    ]

    def get_extra_kwargs(self):
        return dict(case_pk=self.parent.pk)

    def get_pk_list(self):
        pk_list = [
            obj[0] for obj in getattr(self.parent, self.related_field).values_list()
        ]
        return pk_list

    def validate_item(self, item):
        self.assertEqual(self.obj.username, item["username"])

    def test_list_no_users(self):
        self.login_required()
        getattr(self.parent, self.related_field).set([])
        response = self.client.get(self.get_url(name="list", **self.get_extra_kwargs()))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(response.json().get(self.paginated_response_results_key)), 0
        )


class NotifiedUserViewSetTestCase(UserViewSetMixin, OrderingViewSetMixin, TestCase):
    related_field = "notified_users"
    basename = "case-notified_user"


class ResponsibleUserViewSetTestCase(UserViewSetMixin, OrderingViewSetMixin, TestCase):
    related_field = "responsible_users"
    basename = "case-responsible_user"
