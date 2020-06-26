from django.contrib import admin

from .models import Case


class CaseAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'comment',
        'tags',
        'featureoptions',
        'audited_institutions',
        'notified_users',
        'responsible_users',
    )

    autocomplete_fields = [
        "audited_institutions", "notified_users", "responsible_users", "tags"
    ]


admin.site.register(Case, CaseAdmin)
