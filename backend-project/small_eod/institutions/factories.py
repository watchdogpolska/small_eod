from factory.django import DjangoModelFactory
import factory.fuzzy
from .models import AddressData, ExternalIdentifier, Institution


class PolishFaker(factory.Faker):
    def __init__(self, *args, **kwargs):
        kwargs["locale"] = "PL"
        super().__init__(*args, **kwargs)


class AddressDataFactory(DjangoModelFactory):
    city = PolishFaker("city")
    voivodeship = PolishFaker("region")
    flat_no = PolishFaker("building_number")
    street = PolishFaker("street_name")
    postal_code = PolishFaker("postcode")
    house_no = PolishFaker("building_number")
    email = PolishFaker("email")
    epuap = factory.Sequence(lambda n: "epuap-%s" % n)  # todo provide example epuap

    class Meta:
        model = AddressData


class ExternalIdentifierFactory(DjangoModelFactory):
    # todo
    class Meta:
        model = ExternalIdentifier


class InstitutionFactory(DjangoModelFactory):
    # todo
    class Meta:
        model = Institution
