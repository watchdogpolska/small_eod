from django.test import TestCase

from ...generic.tests.test_serializers import ResourceSerializerMixin
from ..factories import AdministrativeUnitFactory
from ..serializers import AdministrativeUnitSerializer


class AdministrativeUnitSerializerTestCase(ResourceSerializerMixin, TestCase):
    serializer_class = AdministrativeUnitSerializer
    factory_class = AdministrativeUnitFactory
