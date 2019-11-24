from django.contrib import admin
from import_export.admin import ImportExportMixin

from small_eod.extracts.models import Mail


class MailAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        "subject",
        "to_address",
        "from_address",
        "text",
        "attachments_count",
        "date",
    ]
    search_fields = ["subject", "to_address", "from_address"]
    list_filter = ["attachments_count"]


admin.site.register(Mail, MailAdmin)
