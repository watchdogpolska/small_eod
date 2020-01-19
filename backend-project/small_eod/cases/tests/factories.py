from django.test import TestCase

from ..factories import CaseFactory
from ..models import Case
from ...dictionaries.factories import FeatureFactory
from ...generic.tests.factories import FactoryTestCaseMixin
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
