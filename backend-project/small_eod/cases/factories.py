import factory

from .models import Case


class CaseFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: "case-%04d" % n)
    comment = factory.Sequence(lambda n: "comment-%04d" % n)

    class Meta:
        model = Case
