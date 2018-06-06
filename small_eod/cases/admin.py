from django.contrib import admin

# Register your models here.
from small_eod.cases.models import Letter, Institution, Case


class LetterInline(admin.TabularInline):
    fields = ("identifier", "name", "attachment", "institution",
              "ordering",)
    sortable_field_name = "ordering"
    model = Letter
    extra = 0


class CaseAdmin(admin.ModelAdmin):
    inlines = [LetterInline]
    list_display = ['name', 'comment', 'created', 'modified']


class InstitutionAdmin(admin.ModelAdmin):
    list_display = ['name', 'comment', 'created', 'modified']
    search_fields = ['name', 'comment']


class LetterAdmin(admin.ModelAdmin):
    list_display = ['name', 'comment', 'created', 'modified']
    list_filter = ['institution', 'direction']
    search_fields = ['name', 'comment', 'identifier']


admin.site.register(Case, CaseAdmin)
admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Letter, LetterAdmin)
