from django.contrib import admin
from django.db import models
from django.forms import widgets
from django.utils.encoding import force_text
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportMixin

from small_eod.cases.models import Letter, Institution, Case, Channel, Tag, Person, Dictionary
from small_eod.cases.resources import InstitutionResource, TagResource


def display_tags(obj):
    return ", ".join(force_text(x) for x in obj.tags.all()) or '-'


display_tags.short_description = _("Tags")


class LetterInline(admin.StackedInline):
    sortable_field_name = "ordering"
    model = Letter
    extra = 0


class InstitutionTagFilter(admin.RelatedOnlyFieldListFilter):

    def __init__(self, field, request, params, model, model_admin, field_path):
        super().__init__(field, request, params, model, model_admin, field_path)
        self.title = _("Institution tags by letters")


class CaseAdmin(admin.ModelAdmin):
    inlines = [LetterInline]
    list_display = ['name', 'comment', 'created', 'modified', display_tags]
    list_filter = ['responsible_people', 'tags',
                   ('letter__institution__tags', InstitutionTagFilter)]
    raw_id_fields = ['responsible_people', 'tags']

    formfield_overrides = {
        models.ManyToManyField: {'widget': widgets.CheckboxSelectMultiple},
    }

    autocomplete_lookup_fields = {
        # 'fk': ['responsible_people'],
        'm2m': ['responsible_people', 'tags'],
    }


class InstitutionAdmin(ImportExportMixin, admin.ModelAdmin):
    raw_id_fields = ['tags']
    list_display = ['name', 'comment', 'created', 'modified', display_tags]
    search_fields = ['name', 'comment']

    resource_class = InstitutionResource

    autocomplete_lookup_fields = {
        'm2m': ['tags'],
    }


class LetterAdmin(admin.ModelAdmin):
    list_display = ['name', 'direction', 'institution', 'data', 'identifier', 'case', 'comment', 'created', 'modified',
                    'channel', display_tags]
    list_filter = ['institution', 'direction', 'case', 'channel']
    search_fields = ['name', 'comment', 'identifier', 'institution__name', 'comment']

    raw_id_fields = ['institution', 'case', 'tags']

    autocomplete_lookup_fields = {
        'fk': ['institution', 'case'],
        'm2m': ['tags'],
    }


class TagAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = TagResource


admin.site.register(Person)
admin.site.register(Dictionary)
admin.site.register(Tag, TagAdmin)
admin.site.register(Channel)
admin.site.register(Case, CaseAdmin)
admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Letter, LetterAdmin)
