import string

import factory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyText
from teryt_tree.factories import JednostkaAdministracyjnaFactory

from .models import AddressData, ExternalIdentifier, Institution
from ..generic.factories import AbstractTimestampUserFactory, FuzzyRegon, PolishFaker


class ExternalIdentifierFactory(DjangoModelFactory):

    regon = FuzzyRegon()
    nip = FuzzyText(length=10, chars=string.digits)

    class Meta:
        model = ExternalIdentifier


class AddressDataFactory(DjangoModelFactory):

    city = PolishFaker("city")
    flat_no = PolishFaker("building_number")
    street = PolishFaker("street_name")
    postal_code = PolishFaker("postcode")
    house_no = PolishFaker("building_number")
    email = PolishFaker("email")
    epuap = factory.Sequence(lambda n: "/epuap-%04d/SkrytkaESP" % n)

    class Meta:
        model = AddressData


class InstitutionFactory(AbstractTimestampUserFactory, DjangoModelFactory):

    address = factory.SubFactory(AddressDataFactory)
    name = factory.Sequence(lambda n: "name-%04d" % n)
    external_identifier = factory.SubFactory(ExternalIdentifierFactory)
    administrative_unit = factory.SubFactory(JednostkaAdministracyjnaFactory)

    class Meta:
        model = Institution
