from test_plus.test import TestCase

from ..factories import UserFactory
from ..serializers import UserSerializer
from ...generic.tests.test_views import ReadOnlyViewSetMixin


class UserViewSetTestCase(ReadOnlyViewSetMixin, TestCase):
    basename = "user"
    serializer_class = UserSerializer
    factory_class = UserFactory
    queries_less_than_limit = 5

    def validate_item(self, item):
        self.assertEqual(item["username"], self.obj.username)
