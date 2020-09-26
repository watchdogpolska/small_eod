from unittest import TestCase
from django.db.models import Q
from ..grammar import parse
from .fixtures import DemoSearchSet


class BaseFilterSetTestCase(TestCase):
    def setUp(self):
        self.instance = DemoSearchSet()

    def assertCondition(self, querystring, expected):
        self.assertEqual(self.instance.get_condition(parse(querystring)), expected)

    def test_simple_keyword(self):
        self.assertCondition(
            "term1 OR term2", Q(name__icontains="term1") | Q(name__icontains="term2")
        )

    def test_complex_keyword(self):
        self.assertCondition(
            "term1 OR ( term2 AND term3 )",
            Q(name__icontains="term1")
            | Q(Q(name__icontains="term2") & Q(name__icontains="term3")),
        )

    def test_filter(self):
        self.assertCondition("a:b OR term2", Q(a="b") | Q(name__icontains="term2"))
