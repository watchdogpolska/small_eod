from django.test import TestCase

from ...generic.tests.test_serializers import ResourceSerializerMixin
from ..factories import UserFactory
from ..serializers import UserSerializer, TokenResponseSerializer


class UserSerializerTestCase(ResourceSerializerMixin, TestCase):
    serializer_class = UserSerializer
    factory_class = UserFactory
