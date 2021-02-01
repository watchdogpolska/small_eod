from django import forms
from django.core.exceptions import ValidationError
from pyparsing import ParseException

from .grammar import parse


class SearchField(forms.CharField):
    def clean(self, *args, **kwargs):
        value = super().clean(*args, **kwargs)
        if not value:
            return ""
        try:
            return parse(value)
        except ParseException as e:
            raise ValidationError(str(e))
