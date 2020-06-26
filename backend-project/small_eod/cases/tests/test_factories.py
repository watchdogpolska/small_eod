from django.test import TestCase

from ..factories import CaseFactory
from ..models import Case
from ...features.factories import FeatureOptionFactory
from ...generic.tests.mixins import FactoryTestCaseMixin
from ...institutions.factories import InstitutionFactory
from ...tags.factories import TagFactory
from ...users.factories import UserFactory


class CaseFactoryTestCase(FactoryTestCaseMixin, TestCase):
    MODEL = Case
    FACTORY = CaseFactory
    FACTORY_COUNT = 2  # its slow

    @classmethod
    def create_factory(cls):
        return cls.FACTORY.create(
            audited_institutions__size=2,
            responsible_users__size=2,
            notified_users__size=2,
            tags__size=2,
            featureoptions__size=2,
        )

    def test_set_implicit_many_to_many(self):
        case = self.create_factory()

        self.assertEqual(case.audited_institutions.count(), 2)
        self.assertEqual(case.responsible_users.count(), 2)
        self.assertEqual(case.notified_users.count(), 2)
        self.assertEqual(case.tags.count(), 2)
        self.assertEqual(case.featureoptions.count(), 2)

    def test_set_explicit_many_to_many(self):
        """
        Check if related objects are created.
        """
        audited_institutions = InstitutionFactory.create_batch(size=2)
        responsible_users = UserFactory.create_batch(size=2)
        notified_users = UserFactory.create_batch(size=2)
        tags = TagFactory.create_batch(size=2)
        featureoptions = FeatureOptionFactory.create_batch(size=2)

        case = self.FACTORY.create(
            audited_institutions=audited_institutions,
            responsible_users=responsible_users,
            notified_users=notified_users,
            tags=tags,
            featureoptions=featureoptions,
        )

        self.assertCountEqual(audited_institutions, case.audited_institutions.all())
        self.assertCountEqual(responsible_users, case.responsible_users.all())
        self.assertCountEqual(notified_users, case.notified_users.all())
        self.assertCountEqual(tags, case.tags.all())
        self.assertCountEqual(featureoptions, case.featureoptions.all())
