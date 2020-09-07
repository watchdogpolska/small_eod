from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _

from .models import Letter
from ..files.models import File


def link_to_case(obj):
    if not obj.case_id:
        return None
    url = reverse("admin:cases_case_changelist") + "?pk__exact=" + str(obj.case_id)
    return format_html('<a href="{}">{}</a>'.format(url, obj.case))


link_to_case.short_description = _("Case")


def get_attachment_status(obj):
    return bool(obj.attachments.all())


get_attachment_status.short_description = _("Attachment")
get_attachment_status.boolean = True


class FileInlineAdmin(admin.TabularInline):
    model = File
    extra = 1


class LetterAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "document_type",
        "direction",
        "institution",
        "date",
        "final",
        "comment",
        "created_on",
        "modified_on",
        "excerpt",
        "reference_number",
        link_to_case,
        "channel",
        "institution",
        get_attachment_status,
    ]
    inlines = [FileInlineAdmin]

    list_filter = ["institution",
                   "document_type",
                   "direction",
                   "case",
                   "channel"]

    search_fields = [
        "document_type__name",
        "comment",
        "reference_number",
        "institution__name",
        "case__name",
    ]

    raw_id_fields = ["institution", "case"]

    autocomplete_lookup_fields = {
        "fk": ["institution", "case"],
    }

    def get_queryset(self, request):
        return (
            super()
            .get_queryset(request)
            .select_related("channel", "institution", "case")
        )


admin.site.register(Letter, LetterAdmin)
