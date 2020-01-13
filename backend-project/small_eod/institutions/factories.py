import string

import factory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyText
from teryt_tree.factories import JednostkaAdministracyjnaFactory

from .models import AddressData, ExternalIdentifier, Institution
from ..generic.factories import AbstractTimestampUserFactory


class PolishFaker(factory.Faker):
    def __init__(self, *args, **kwargs):
        kwargs["locale"] = "PL"
        super().__init__(*args, **kwargs)


class FuzzyRegon(factory.fuzzy.BaseFuzzyAttribute):
    def __init__(self):
        super().__init__()
        self.chars_10 = FuzzyText(length=10, chars=string.digits)
        self.chars_14 = FuzzyText(length=14, chars=string.digits)

    def fuzz(self):
        return factory.random.randgen.choice([self.chars_10, self.chars_14,]).fuzz()


class AddressDataFactory(DjangoModelFactory):
    city = PolishFaker("city")
    voivodeship = PolishFaker("region")
    flat_no = PolishFaker("building_number")
    street = PolishFaker("street_name")
    postal_code = PolishFaker("postcode")
    house_no = PolishFaker("building_number")
    email = PolishFaker("email")
    epuap = factory.Sequence(lambda n: "/epuap-%04s/SkrytkaESP" % n)

    class Meta:
        model = AddressData


class ExternalIdentifierFactory(DjangoModelFactory):
    nip = FuzzyText(length=10, chars=string.digits)
    regon = FuzzyRegon()

    class Meta:
        model = ExternalIdentifier


class InstitutionFactory(AbstractTimestampUserFactory, DjangoModelFactory):
    name = factory.Sequence(lambda n: "name-%04s" % n)
    external_identifier = factory.SubFactory(ExternalIdentifierFactory)
    administrative_unit = factory.SubFactory(JednostkaAdministracyjnaFactory)
    address = factory.SubFactory(AddressDataFactory)

    class Meta:
        model = Institution
