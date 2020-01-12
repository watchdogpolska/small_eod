from typing import Tuple, Type

from django.db.models import Model
from django.test import TestCase, tag
from factory.django import DjangoModelFactory

from . import tags


class FactoryTestCase(TestCase):

    FACTORIES: Tuple[Tuple[Type[Model], Type[DjangoModelFactory]]] = ()
    FACTORIES_MANY: int = 10

    @tag(tags.FACTORY_SINGLE)
    def test_factories_simple(self):
        for e in self.FACTORIES:
            model, factory = e[0], e[1]
            obj = factory(); obj.save()
            self.assertEqual(
                1,
                model.objects.all().count(),
            )
            print(f"Created model {model} with factory {factory}")

    @tag(tags.FACTORY_MANY)
    def test_factories_many(self):
        for e in self.FACTORIES:
            model, factory = e[0], e[1]
            for x in range(1, self.FACTORIES_MANY):
                obj = factory(); obj.save()
                self.assertEqual(
                    x,
                    model.objects.all().count(),
                )
                print(f"Created model {model} with factory {factory}")
