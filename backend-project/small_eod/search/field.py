from django import forms
from .grammar import parse
from pyparsing import ParseException
from django.core.exceptions import ValidationError


class SearchField(forms.CharField):
    def clean(self, *args, **kwargs):
        value = super().clean(*args, **kwargs)
        if not value:
            return ""
        try:
            return parse(value)
        except ParseException as e:
            raise ValidationError(str(e))
