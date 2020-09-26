from django.db.models import Q
from .grammar import (
    OperationAnd,
    OperationOr,
    OperationNot,
    SearchTerm,
    FieldExpr,
)


class BaseSearchSet:
    search_fields = None
    filters = {}

    def get_term_condition(self, term):
        if not self.search_fields:
            raise NotImplementedError(
                "search_fields or get_term_match must be overridden"
            )
        condition = Q()
        for field_name in self.search_fields:
            condition = condition | Q(**{f"{field_name}__icontains": term})
        return condition

    def get_field_condition(self, term):
        filters = self.get_filters()
        if term.field not in filters:
            raise NotImplementedError(f"Unknown field {term.field}")
        return filters[term.field](term.value)

    def get_filters(self):
        return self.filters

    def get_condition(self, result):
        if isinstance(result, SearchTerm):
            return self.get_term_condition(result.term)
        elif isinstance(result, OperationAnd):
            return self.get_condition(result.operands[0]) & self.get_condition(
                result.operands[1]
            )
        elif isinstance(result, OperationOr):
            return self.get_condition(result.operands[0]) | self.get_condition(
                result.operands[1]
            )
        elif isinstance(result, OperationNot):
            return ~self.get_condition(result.operands)
        elif isinstance(result, FieldExpr):
            return self.get_field_condition(result)
        raise RuntimeError(f"Unknown operation {result.__class__.__name__}")


def create_searchset(search_fields, filters):
    searchset = BaseSearchSet()
    searchset.search_fields = search_fields
    searchset.filters = filters
    return searchset
