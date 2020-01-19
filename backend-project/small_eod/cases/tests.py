from django.test import TestCase

from .factories import CaseFactory
from .models import Case
from .serializers import CaseSerializer, CaseCountSerializer
from ..dictionaries.factories import FeatureFactory, DictionaryFactory
from ..generic.tests import (
    GenericViewSetMixin,
    FactoryCreateObjectsMixin,
    ReadOnlyViewSetMixin,
)
from ..institutions.factories import InstitutionFactory
from ..tags.factories import TagFactory
from ..tags.models import Tag
from ..users.factories import UserFactory
from ..users.serializers import UserSerializer
from rest_framework.test import APIRequestFactory, force_authenticate
from ..notes.factories import NoteFactory


class CaseFactoryTestCase(FactoryCreateObjectsMixin, TestCase):
    MODEL = Case
    FACTORY = CaseFactory
    FACTORY_COUNT = 2  # its slow

    @classmethod
    def create_factory(cls):
        return cls.FACTORY.create(
            audited_institutions=InstitutionFactory.create_batch(size=2),
            responsible_users=UserFactory.create_batch(size=2),
            notified_users=UserFactory.create_batch(size=2),
            tags=TagFactory.create_batch(size=2),
            features=FeatureFactory.create_batch(size=2),
        )

    def test_many_to_many(self):
        """
        Check if related objects are created.
        """
        audited_institutions = InstitutionFactory.create_batch(size=2)
        responsible_users = UserFactory.create_batch(size=2)
        notified_users = UserFactory.create_batch(size=2)
        tags = TagFactory.create_batch(size=2)
        features = FeatureFactory.create_batch(size=2)

        case = self.FACTORY.create(
            audited_institutions=audited_institutions,
            responsible_users=responsible_users,
            notified_users=notified_users,
            tags=tags,
            features=features,
        )

        self.assertCountEqual(audited_institutions, case.audited_institution.all())
        self.assertCountEqual(responsible_users, case.responsible_user.all())
        self.assertCountEqual(notified_users, case.notified_user.all())
        self.assertCountEqual(tags, case.tag.all())
        self.assertCountEqual(features, case.feature.all())


class CaseCountSerializerTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        factory = APIRequestFactory()
        self.request = factory.get("/")
        force_authenticate(self.request, user=self.user)
        self.request.user = self.user

    def get_default_data(self, new_data=None, skip=None):
        new_data = new_data or {}
        skip = skip or []
        default_data = {
            "name": "Polska Fundacja Narodowa o rejestr umów",
            "audited_institution": [],
            "comment": "xxx",
            "responsible_user": [],
            "notified_user": [],
            "feature": [],
            "tag": ["rejestr umów"],
        }
        for field in skip:
            del default_data[field]
        return {
            **default_data,
            **new_data,
        }

    def test_tag_field(self):
        serializer = CaseSerializer(
            data=self.get_default_data(), context={"request": self.request}
        )
        self.assertTrue(serializer.is_valid(), serializer.errors)
        obj = serializer.save()
        self.assertTrue(Tag.objects.count(), 1)
        self.assertEqual(obj.tag.all()[0].name, "rejestr umów")
        data = CaseSerializer(Case.objects.get()).data
        self.assertTrue(data["tag"], ["rejestr umów"])

    def test_raise_for_over_maximum_feature(self):
        dictionary = DictionaryFactory(max_items=3)
        features = FeatureFactory.create_batch(size=5, dictionary=dictionary)
        serializer = CaseCountSerializer(
            data=self.get_default_data(
                {"feature": [x.id for x in features], "tag": []}
            ),
            context={"request": self.request},
        )
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors.keys()), {"feature"})

    def test_serializer_counters(self):
        NoteFactory()
        case_counted = Case.objects.with_counter().get()
        self.assertEqual(case_counted.letter_count, 0)
        self.assertEqual(case_counted.note_count, 1)
        data = CaseCountSerializer(case_counted).data
        self.assertEqual(data["letter_count"], 0)
        self.assertEqual(data["note_count"], 1)

    def test_default_for_related_user(self):
        serializer = CaseCountSerializer(
            data=self.get_default_data(skip=["responsible_user", "notified_user"]),
            context={"request": self.request},
        )
        self.assertTrue(serializer.is_valid(), serializer.errors)
        obj = serializer.save()
        self.assertCountEqual(obj.responsible_user.all(), [self.user])
        self.assertCountEqual(obj.notified_user.all(), [self.user])


    def test_save_related_user(self):
        [responsible_user, notified_user] = UserFactory.create_batch(size=2)
        serializer = CaseCountSerializer(
            data=self.get_default_data(
                new_data={
                    "responsible_user": [responsible_user.pk],
                    "notified_user": [notified_user.pk],
                }
            ),
            context={"request": self.request},
        )
        self.assertTrue(serializer.is_valid(), serializer.errors)
        obj = serializer.save()
        self.assertCountEqual(obj.responsible_user.all(), [responsible_user])
        self.assertCountEqual(obj.notified_user.all(), [notified_user])


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

