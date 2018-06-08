from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportMixin

from small_eod.cases.models import Letter, Institution, Case, Channel, Tag, Person
from small_eod.cases.resources import InstitutionResource


class LetterInline(admin.TabularInline):
    fields = ("identifier", "name", "attachment", "institution",
              "ordering", "data", "case")
    sortable_field_name = "ordering"
    model = Letter
    extra = 0


class CaseAdmin(admin.ModelAdmin):
    inlines = [LetterInline]
    list_display = ['name', 'comment', 'created', 'modified']

    raw_id_fields = ['responsible_people']

    autocomplete_lookup_fields = {
        # 'fk': ['responsible_people'],
        'm2m': ['responsible_people'],
    }


class InstitutionAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name', 'comment', 'created', 'modified']
    search_fields = ['name', 'comment']
    resource_class = InstitutionResource

    raw_id_fields = ['tags']

    autocomplete_lookup_fields = {
        'm2m': ['tags'],
    }


class LetterAdmin(admin.ModelAdmin):
    list_display = ['name', 'direction', 'institution', 'data', 'identifier', 'case', 'comment', 'created', 'modified',
                    'channel']
    list_filter = ['institution', 'direction', 'case', 'channel']
    search_fields = ['name', 'comment', 'identifier', 'institution__name', 'comment']

    raw_id_fields = ['institution', 'case', 'tags']

    autocomplete_lookup_fields = {
        'fk': ['institution', 'case'],
        'm2m': ['tags'],
    }


admin.site.register(Person)
admin.site.register(Tag)
admin.site.register(Channel)
admin.site.register(Case, CaseAdmin)
admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Letter, LetterAdmin)
