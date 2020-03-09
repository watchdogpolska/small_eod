from django.test import TestCase
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
            path=self.get_url_detail(),
            HTTP_AUTHORIZATION=f"Bearer {token}",
        )
        self.assertEqual(resp.status_code, 200)


class CollectionViewSetTestCase(
    TokenAuthorizationTestCaseMixin, GenericViewSetMixin, TestCase
):

    basename = "collection"
    serializer_class = CollectionSerializer
    factory_class = CollectionFactory

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


class NoteViewSetTestCase(
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


class CaseViewSetTestCase(
    TokenAuthorizationTestCaseMixin, ReadOnlyViewSetMixin, TestCase
):

    basename = "collection-cases"
    factory_class = CaseFactory

    def setUp(self):
        super().setUp()
        self.collection = CollectionFactory(query=str(self.obj.id))

    def get_extra_kwargs(self):
        return dict(collection_pk=self.collection.pk)

    def validate_item(self, item):
        self.assertEqual(self.obj.name, item["name"])
