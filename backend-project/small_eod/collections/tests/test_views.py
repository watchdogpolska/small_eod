from test_plus.test import TestCase
from django.urls import reverse

from ..factories import CollectionFactory
from ..serializers import CollectionSerializer
from ...generic.tests.test_views import ReadOnlyViewSetMixin, GenericViewSetMixin
from ...notes.factories import NoteFactory
from ...cases.factories import CaseFactory
from ...users.mixins import AuthenticatedMixin


class TokenAuthorizationTestCaseMixin:
    def get_collection(self):
        return self.collection

    def test_require_authentication(self):
        resp = self.client.get(self.get_url(name="list", **self.get_extra_kwargs()))
        self.assertEqual(resp.status_code, 401)

    def test_authorize_with_token(self):
        self.login_required()
        resp = self.client.post(
            path=reverse(
                "collection-tokens-list",
                kwargs={"collection_pk": self.get_collection().pk},
            ),
            content_type="application/json",
        )
        self.assertEqual(resp.status_code, 201)
        token = resp.json()["accessToken"]

        self.client.logout()

        resp = self.client.get(
            path=self.get_url_detail(), data={"authorization": token},
        )
        self.assertEqual(resp.status_code, 200)


class CollectionViewSetTestCase(
    TokenAuthorizationTestCaseMixin, GenericViewSetMixin, TestCase
):

    basename = "collection"
    serializer_class = CollectionSerializer
    factory_class = CollectionFactory
    queries_less_than_limit = 7

    def get_collection(self):
        return self.obj

    def validate_item(self, item):
        self.assertEqual(item["comment"], self.obj.comment)


class TokenCreateAPIView(AuthenticatedMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.collection = CollectionFactory()

    def test_refuse_non_authenticated(self):
        resp = self.client.post(
            path=reverse(
                "collection-tokens-list", kwargs={"collection_pk": self.collection.pk}
            ),
            content_type="application/json",
        )
        self.assertEqual(resp.status_code, 401, resp.json())

    def test_accept_authenticated(self):
        self.login_required()
        resp = self.client.post(
            path=reverse(
                "collection-tokens-list", kwargs={"collection_pk": self.collection.pk}
            ),
            content_type="application/json",
        )
        self.assertEqual(resp.status_code, 201, resp.json())


class NoteCollectionViewSetTestCase(
    TokenAuthorizationTestCaseMixin, ReadOnlyViewSetMixin, TestCase
):
    basename = "collection-note"
    factory_class = NoteFactory
    queries_less_than_limit = 7

    def setUp(self):
        super().setUp()
        self.collection = CollectionFactory(query=str(self.obj.case.id))

    def get_extra_kwargs(self):
        return dict(collection_pk=self.collection.pk, case_pk=self.obj.case.pk)

    def validate_item(self, item):
        self.assertEqual(self.obj.comment, item["comment"])

    def test_num_queries_for_list(self):
        self.login_required()
        with self.assertNumQueriesLessThan(self.queries_less_than_limit):
            response = self.client.get(self.get_url_list())
        self.assertEqual(response.status_code, 200)

        NoteFactory(case=self.obj.case)
        with self.assertNumQueriesLessThan(self.queries_less_than_limit):
            response = self.client.get(self.get_url_list())
        self.assertEqual(response.status_code, 200)


class CaseCollectionViewSetTestCase(
    TokenAuthorizationTestCaseMixin, ReadOnlyViewSetMixin, TestCase
):

    basename = "collection-cases"
    factory_class = CaseFactory
    queries_less_than_limit = 16

    def setUp(self):
        super().setUp()
        self.collection = CollectionFactory(query=str(self.obj.id))

    def get_extra_kwargs(self):
        return dict(collection_pk=self.collection.pk)

    def validate_item(self, item):
        self.assertEqual(self.obj.name, item["name"])

