from django.core.validators import BaseValidator
from django.utils.translation import ugettext_lazy as _


class ExactLengthsValidator(BaseValidator):
    message = _(
        "Ensure this value has length of any %(limit_value)s (it has %(show_value)d)."
    )

    def __init__(self, limit_value: list = None, **kwargs):
        super().__init__(limit_value=limit_value, **kwargs)

    def compare(self, a, b):
        return all(a != x for x in b)

    def clean(self, x):
        return len(x)
