import factory.fuzzy
from factory.django import DjangoModelFactory

from .models import Key, Scope
from ..users.factories import UserFactory


class KeyFactory(DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def scopes(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            for scope in extracted:
                self.scopes.add(ScopeFactory(name=scope))

    class Meta:
        model = Key


class ScopeFactory(DjangoModelFactory):
    name = factory.Sequence(lambda n: "scope-%04d" % n)

    class Meta:
        model = Scope
        django_get_or_create = ("name",)
