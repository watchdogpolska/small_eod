from test_plus.test import TestCase
from django.urls import reverse

from ..factories import CollectionFactory
from ..serializers import CollectionSerializer
from ...generic.tests.test_views import (
    ReadOnlyViewSetMixin,
    GenericViewSetMixin,
    OrderingViewSetMixin,
)
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
            path=self.get_url_detail(),
            data={"authorization": token},
        )
        self.assertEqual(resp.status_code, 200)


class CollectionViewSetTestCase(
    TokenAuthorizationTestCaseMixin, GenericViewSetMixin, OrderingViewSetMixin, TestCase
):

    basename = "collection"
    serializer_class = CollectionSerializer
    factory_class = CollectionFactory
    ordering_fields = ["name", "-public", "expired_on,name"]

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

    def setUp(self):
        super().setUp()
        self.collection = CollectionFactory(query=str(self.obj.case.id))

    def get_extra_kwargs(self):
        return dict(collection_pk=self.collection.pk, case_pk=self.obj.case.pk)

    def validate_item(self, item):
        self.assertEqual(self.obj.comment, item["comment"])

    def increase_list(self):
        children = self.factory_class.create_batch(case=self.obj.case, size=5)
        self.collection.query = ",".join(
            [str(child.case.pk) for child in children] + [self.collection.query]
        )


class CaseCollectionViewSetTestCase(
    TokenAuthorizationTestCaseMixin, ReadOnlyViewSetMixin, TestCase
):

    basename = "collection-case"
    factory_class = CaseFactory
    queries_less_than_limit = 11

    def setUp(self):
        super().setUp()
        self.collection = CollectionFactory(query=str(self.obj.id))

    def get_extra_kwargs(self):
        return dict(collection_pk=self.collection.pk)

    def validate_item(self, item):
        self.assertEqual(self.obj.name, item["name"])

    def increase_list(self):
        children = self.factory_class.create_batch(size=5)
        self.collection.query = ",".join(
            [str(child.pk) for child in children] + [self.collection.query]
        )
        self.collection.save()
