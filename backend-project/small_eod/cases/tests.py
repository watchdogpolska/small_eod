from django.test import TestCase

from .factories import CaseFactory
from .models import Case
from .serializers import CaseSerializer, CaseCountSerializer
from ..dictionaries.factories import FeatureFactory, DictionaryFactory
from ..generic.tests import GenericViewSetMixin, FactoryCreateObjectsMixin
from ..institutions.factories import InstitutionFactory
from ..tags.factories import TagFactory
from ..tags.models import Tag
from ..users.factories import UserFactory


class CaseFactoryTestCase(FactoryCreateObjectsMixin, TestCase):
    MODEL = Case
    FACTORY = CaseFactory
    FACTORY_COUNT = 2   # its slow

    @classmethod
    def create_factory(cls):
        return cls.FACTORY.create(
            audited_institutions=(InstitutionFactory(), InstitutionFactory(),),
            responsible_users=(UserFactory(), UserFactory(),),
            notified_users=(UserFactory(), UserFactory(),),
            tags=(TagFactory(), TagFactory(),),
        )

    def test_many_to_many(self):
        """
        Check if related objects are created.
        """
        audited_institutions = (
            InstitutionFactory(), InstitutionFactory(),
        )
        responsible_users = (
            UserFactory(), UserFactory(),
        )
        notified_users = (
            UserFactory(), UserFactory(),
        )
        tags = (
            TagFactory(), TagFactory(),
        )

        case = self.FACTORY.create(
            audited_institutions=audited_institutions,
            responsible_users=responsible_users,
            notified_users=notified_users,
            tags=tags,
        )

        self.assertEqual(audited_institutions, tuple(case.audited_institution.all()))
        self.assertEqual(responsible_users, tuple(case.responsible_user.all()))
        self.assertEqual(notified_users, tuple(case.notified_user.all()))
        self.assertEqual(tags, tuple(case.tag.all()))


class CaseCountSerializerTestCase(TestCase):
    def test_tag_field(self):
        serializer = CaseSerializer(data={
            "name": "Polska Fundacja Narodowa o rejestr umów",
            "audited_institution": [],
            "comment": "xxx",
            "responsible_user": [],
            "notified_user": [],
            "feature": [],
            "tag": ["rejestr umów"],
        })
        self.assertTrue(serializer.is_valid(), serializer.errors)
        obj = serializer.save()
        self.assertTrue(Tag.objects.count(), 1)
        self.assertEqual(obj.tag.all()[0].name, "rejestr umów")
        data = CaseSerializer(Case.objects.get()).data
        self.assertTrue(data["tag"], ["rejestr umów"])

    def test_raise_for_over_maximum_feature(self):
        dictionary = DictionaryFactory(max_items=3)
        features = FeatureFactory.create_batch(size=5, dictionary=dictionary)
        serializer = CaseCountSerializer(data={
            "name": "Polska Fundacja Narodowa o rejestr umów",
            "audited_institution": [],
            "comment": "xxx",
            "responsible_user": [],
            "notified_user": [],
            "feature": [x.id for x in features],
            "tag": [],
        })
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors.keys()), {'feature'})

    def test_serializer_counters(self):
        CaseFactory()
        case_counted = Case.objects.with_counter().get()
        self.assertEqual(case_counted.letter_count, 0)
        self.assertEqual(case_counted.note_count, 0)
        data = CaseCountSerializer(case_counted).data
        self.assertEqual(data["letter_count"], 0)
        self.assertEqual(data["note_count"], 0)


class CaseViewSetTestCase(GenericViewSetMixin, TestCase):
    basename = 'case'
    serializer_class = CaseSerializer
    factory_class = CaseFactory

    def validate_item(self, item):
        self.assertEqual(item["name"], self.obj.name)
