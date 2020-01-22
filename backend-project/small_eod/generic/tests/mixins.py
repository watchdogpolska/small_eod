from typing import Type

from django.db.models import Model
from django.test import tag
from factory.django import DjangoModelFactory


class FactoryTestCaseMixin:
    FACTORY = Type[DjangoModelFactory]
    MODEL = Type[Model]

    FACTORY_COUNT = 2

    @classmethod
    def create_factory(cls):
        return cls.FACTORY()

    def _test_factory_object(self, msg, count):
        obj = self.create_factory()
        self.assertEqual(
            count,
            self.MODEL.objects.all().count(),
            msg=f"Failed {msg} factory test - "
            f"position: {count} "
            f"model: {self.MODEL} "
            f"factory: {self.FACTORY} "
            f"object: {obj}",
        )

    @tag("FactoryCreateObjectsMixin")
    def test_factories_simple(self):
        self._test_factory_object(msg="simple", count=1)

    @tag("FactoryCreateObjectsMixin")
    def test_factories_many(self):
        for x in range(1, self.FACTORY_COUNT):
            self._test_factory_object(msg="many", count=x)

    # def test_print_to_console(self):
    #     """
    #     Show in the console how the data looks like.
    #     Just making sure that frontend has the right data
    #     to work with.
    #     """
    #     from django.forms import model_to_dict
    #     print(f"\n{model_to_dict(self.create_factory())}")
