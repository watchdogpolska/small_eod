import unicodedata
from os.path import basename

import requests
import zipstream
from django.contrib import admin
from django.http import StreamingHttpResponse
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _

from ..files.models import File
from .models import DocumentType, Letter, ReferenceNumber


def link_to_case(obj):
    if not obj.case_id:
        return None
    url = reverse("admin:cases_case_changelist") + "?pk__exact=" + str(obj.case_id)
    return format_html(f'<a href="{url}">{obj.case}</a>')


link_to_case.short_description = _("Case")


def get_attachment_status(obj):
    return bool(obj.attachments.all())


get_attachment_status.short_description = _("Attachment")
get_attachment_status.boolean = True


def download_selected_letters(modeladmin, request, queryset):
    z = zipstream.ZipFile()
    for letter in queryset:
        if letter.attachments.all().exists():
            case_name = letter.case.name if letter.case else "unknown"
            case_name = unicodedata.normalize("NFKD", case_name.replace("/", "__"))
            case_id = letter.case.id or "unknown"
            ordering = 0
            for file in letter.attachments.all():
                file_path = file.path
                filename = basename(file_path)
                ordering += 1
                r = requests.get(file_path, stream=True)

                z.write_iter(
                    f"{case_id}-{case_name}/{ordering:02d}-{filename}",
                    r.iter_content(chunk_size=128),
                )

    response = StreamingHttpResponse(
        streaming_content=z,
        content_type="application/zip",
    )
    response["Content-Disposition"] = 'attachment; filename="letters.zip"'
    return response


download_selected_letters.short_description = _("Download selected letters")


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

    list_filter = ["institution", "document_type", "direction", "case", "channel"]

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

    actions = [download_selected_letters]

    def get_queryset(self, request):
        return (
            super()
            .get_queryset(request)
            .select_related("channel", "institution", "case")
        )


admin.site.register(Letter, LetterAdmin)
admin.site.register(DocumentType)
admin.site.register(ReferenceNumber)
