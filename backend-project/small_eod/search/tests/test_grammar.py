from unittest import TestCase
from pyparsing import pyparsing_test
from ..grammar import (
    searchTerm,
    SearchTerm,
    field_expr,
    FieldExpr,
    search_expr,
    OperationAnd,
    OperationOr,
)


class AssertParserMixin(pyparsing_test.TestParseResultsAsserts):
    def assert_parser(self, expr, test_string, expected):
        result = expr.parseString(test_string, parseAll=False).asList()
        self.assertEqual(result, [expected])


class SearchTermTestCase(AssertParserMixin, TestCase):
    def test_simple(self):
        self.assert_parser(searchTerm, "abc", SearchTerm("abc"))

    def test_unicode(self):
        self.assert_parser(searchTerm, "łódź", SearchTerm("łódź"))


class FieldExprTestCase(AssertParserMixin, TestCase):
    def test_simple(self):
        self.assert_parser(field_expr, "key:value", FieldExpr(["key", "value"]))

    def test_unicode(self):
        self.assert_parser(field_expr, "key:ł", FieldExpr(["key", "ł"]))

    def test_quote(self):
        self.assert_parser(field_expr, 'key:"value"', FieldExpr(["key", "value"]))


class SearchExprTestCase(AssertParserMixin, TestCase):
    def test_simple(self):
        self.assert_parser(
            search_expr,
            "a AND b",
            OperationAnd([[SearchTerm("a"), "AND", SearchTerm("b")]]),
        )

    def test_precedence(self):
        priority = OperationOr([[SearchTerm("b"), "OR", SearchTerm("c")]])

        self.assert_parser(
            search_expr,
            "a AND ( b OR c )",
            OperationAnd([[SearchTerm("a"), "AND", priority]]),
        )

    def test_ignore_filter_quoted(self):
        self.assert_parser(
            search_expr,
            '"a:b"',
            SearchTerm("a:b"),
        )
