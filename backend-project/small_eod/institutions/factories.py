import string

import factory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyText
from teryt_tree.factories import JednostkaAdministracyjnaFactory
from ..generic.factories import ManyToManyPostGeneration
from .models import Institution
from ..generic.factories import AbstractTimestampUserFactory, FuzzyRegon, PolishFaker


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
        JednostkaAdministracyjnaFactory, category__level=3
    )
    tags = ManyToManyPostGeneration("tags")

    class Meta:
        model = Institution
