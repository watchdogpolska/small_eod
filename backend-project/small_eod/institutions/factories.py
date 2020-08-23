import string

import factory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyText
from ..administrative_units.factories import AdministrativeUnitFactory
from ..generic.factories import ManyToManyPostGeneration
from .models import Institution
from ..generic.factories import AbstractTimestampUserFactory, FuzzyRegon, PolishFaker
from ..tags.factories import TagFactory


class InstitutionFactory(AbstractTimestampUserFactory, DjangoModelFactory):
    city = PolishFaker("city")
    flat_no = PolishFaker("building_number")
    street = PolishFaker("street_name")
    postal_code = PolishFaker("postcode")
    house_no = PolishFaker("building_number")
    email = PolishFaker("email")
    epuap = factory.Sequence(lambda n: "/epuap-%04d/SkrytkaESP" % n)
    name = factory.Sequence(lambda n: "name-%04d" % n)
    regon = FuzzyRegon()
    nip = FuzzyText(length=10, chars=string.digits)
    administrative_unit = factory.SubFactory(
        AdministrativeUnitFactory, category__level=3
    )
    comment = factory.Sequence(lambda n: "comment-%04d" % n)
    tags = ManyToManyPostGeneration("tags", size=2, factory_cls=TagFactory)

    class Meta:
        model = Institution
