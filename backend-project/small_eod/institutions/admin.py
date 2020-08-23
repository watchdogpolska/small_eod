from django.contrib import admin

from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import force_text
from .models import Institution


def display_tags(obj):
    return ", ".join(force_text(x) for x in obj.tags.all()) or "-"


display_tags.short_description = _("Tags")


class InstitutionAdmin(admin.ModelAdmin):
    raw_id_fields = ["tags"]
    list_display = ["name", "comment", "created_on", "modified_on", display_tags]
    search_fields = ["name", "comment"]

    autocomplete_lookup_fields = {
        "m2m": ["tags"],
    }


admin.site.register(Institution, InstitutionAdmin)
