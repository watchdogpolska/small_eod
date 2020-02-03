from django.test import TestCase

from ..models import Case
from ..serializers import CaseSerializer, CaseCountSerializer
from ...dictionaries.factories import FeatureFactory, DictionaryFactory
from ...notes.factories import NoteFactory
from ...tags.models import Tag
from ...users.factories import UserFactory
from ...generic.mixins import AuthRequiredMixin


class CaseCountSerializerTestCase(AuthRequiredMixin, TestCase):
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
