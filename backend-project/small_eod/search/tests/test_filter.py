from unittest import mock

from django.db.models import Q
from django.test import SimpleTestCase

from ..filter import SearchFilter
from ..grammar import parse
from .fixtures import DemoSearchSet


class SearchFilterTestCase(SimpleTestCase):
    def test_filtering_lookup_expr(self):
        qs = mock.Mock(spec=["filter"])
        f = SearchFilter(field_name="somefield", searchset=DemoSearchSet())
        result = f.filter(qs, parse("term1"))
        qs.filter.assert_called_once_with(Q(name__icontains="term1"))
        self.assertNotEqual(qs, result)
