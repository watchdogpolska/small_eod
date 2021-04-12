from django.test import TestCase

from ...generic.mixins import AuthRequiredMixin
from ...generic.tests.test_serializers import ResourceSerializerMixin
from ..factories import FeatureFactory
from ..serializers import FeatureSerializer


class FeatureSerializerTestCase(ResourceSerializerMixin, AuthRequiredMixin, TestCase):
    serializer_class = FeatureSerializer
    factory_class = FeatureFactory
