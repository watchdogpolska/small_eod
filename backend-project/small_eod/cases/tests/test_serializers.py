from django.test import TestCase

from ..models import Case
from ..serializers import CaseCountSerializer
from ...features.factories import FeatureOptionFactory, FeatureFactory
from ...notes.factories import NoteFactory
from ...tags.models import Tag
from ...users.factories import UserFactory
from ...generic.mixins import AuthRequiredMixin
from ...generic.tests.test_serializers import ResourceSerializerMixin
from ..factories import CaseFactory


class CaseCountSerializerTestCase(ResourceSerializerMixin, AuthRequiredMixin, TestCase):
    serializer_class = CaseCountSerializer
    factory_class = CaseFactory

    def get_serializer_context(self):
        return {"request": self.request}

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
            "tags": ["rejestr umów"],
        }
        for field in skip:
            del default_data[field]
        return {
            **default_data,
            **new_data,
        }

    def test_tag_field(self):
        self.login_required()
        serializer = self.serializer_class(
            data=self.get_default_data(), context=self.get_serializer_context()
        )
        self.assertTrue(serializer.is_valid(), serializer.errors)
        obj = serializer.save()
        self.assertTrue(Tag.objects.count(), 1)
        self.assertEqual(obj.tags.all()[0].name, "rejestr umów")
        data = self.serializer_class(Case.objects.get()).data
        self.assertTrue(data["tags"], ["rejestr umów"])

    def test_raise_for_over_maximum_feature(self):
        self.login_required()
        feature = FeatureFactory(max_options=3)
        options = FeatureOptionFactory.create_batch(size=5, feature=feature)
        serializer = self.serializer_class(
            data=self.get_default_data(
                {"featureoptions": [x.id for x in options], "tag": []}
            ),
            context=self.get_serializer_context(),
        )
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors.keys()), {"featureoptions"})

    def test_serializer_counters(self):
        self.login_required()
        NoteFactory()
        case_counted = Case.objects.with_counter().get()
        self.assertEqual(case_counted.letter_count, 0)
        self.assertEqual(case_counted.note_count, 1)
        data = self.serializer_class(case_counted).data
        self.assertEqual(data["letter_count"], 0)
        self.assertEqual(data["note_count"], 1)

    def test_default_for_related_user(self):
        self.login_required()
        serializer = self.serializer_class(
            data=self.get_default_data(skip=["responsible_user", "notified_user"]),
            context=self.get_serializer_context(),
        )
        self.assertTrue(serializer.is_valid(), serializer.errors)
        obj = serializer.save()
        self.assertCountEqual(obj.responsible_users.all(), [self.user])
        self.assertCountEqual(obj.notified_users.all(), [self.user])

    def test_save_related_user(self):
        self.login_required()
        [responsible_users, notified_users] = UserFactory.create_batch(size=2)
        serializer = self.serializer_class(
            data=self.get_default_data(
                new_data={
                    "responsible_users": [responsible_users.pk],
                    "notified_users": [notified_users.pk],
                }
            ),
            context=self.get_serializer_context(),
        )
        self.assertTrue(serializer.is_valid(), serializer.errors)
        obj = serializer.save()
        self.assertCountEqual(obj.responsible_users.all(), [responsible_users])
        self.assertCountEqual(obj.notified_users.all(), [notified_users])
