from pyparsing import (
    Word,
    Suppress,
    CaselessLiteral,
    infixNotation,
    pyparsing_unicode,
    removeQuotes,
    opAssoc,
    FollowedBy,
    quotedString,
)


printables = pyparsing_unicode.printables
alphas = pyparsing_unicode.alphas
nums = pyparsing_unicode.nums
alphanums = pyparsing_unicode.alphanums


class FieldExpr:
    def __init__(self, tokens):
        self.field = tokens[0]
        self.value = tokens[1]

    def __repr__(self):
        return f"({self.field}={self.value})"

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and self.field == other.field
            and self.value == other.value
        )


class UnaryOperation:
    "takes one operand,e.g. not"

    def __init__(self, tokens):
        self.op, self.operands = tokens[0]


class BinaryOperation:
    def __init__(self, tokens):
        self.op = tokens[0][1]
        self.operands = tokens[0][0::2]

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and self.op == other.op
            and self.operands[0] == other.operands[0]
            and self.operands[1] == other.operands[1]
        )


class OperationAnd(BinaryOperation):
    def __repr__(self):
        return "(AND {})".format(" ".join(str(oper) for oper in self.operands))


class OperationOr(BinaryOperation):
    def __repr__(self):
        return "(OR {})".format(" ".join(str(oper) for oper in self.operands))


class OperationNot(UnaryOperation):
    def __repr__(self):
        return f"(NOT {self.operands})"


class ImplicitOperator(OperationAnd):
    def __init__(self, tokens):
        self.op = "AND"
        self.operands = tokens


class SearchTerm:
    def __init__(self, tokens):
        if not isinstance(tokens, str):
            tokens = tokens[0]
        self.term = tokens

    def __repr__(self):
        return f"SearchTerm({self.term})"

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.term == other.term


# the grammar
AND, OR, NOT = map(CaselessLiteral, "AND OR NOT".split())

searchTerm = Word(alphanums) | quotedString.setParseAction(removeQuotes)
searchTerm.setParseAction(SearchTerm).setName("term")

field_label = Word(alphas).setName("label") + FollowedBy(":")
field_value = (Word(alphanums) | quotedString.setParseAction(removeQuotes)).setName(
    "value"
)
field_expr = field_label + Suppress(":") + field_value
field_expr.setParseAction(FieldExpr)

search_expr = infixNotation(
    field_expr | searchTerm,
    [
        (NOT, 1, opAssoc.RIGHT, OperationNot),
        (AND, 2, opAssoc.LEFT, OperationAnd),
        (OR, 2, opAssoc.LEFT, OperationOr),
    ],
)


def parse(value):
    return search_expr.parseString(value, parseAll=True).asList()[0]
