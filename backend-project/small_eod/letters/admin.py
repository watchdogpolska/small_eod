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


class FileInlineAdmin(admin.StackedInline):
    model = File


class LetterAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "document_type",
        "direction",
        "institution",
        "date",
        "final",
        "comment",
        "excerpt",
        "reference_number",
        link_to_case,
        "channel",
        "institution",
        get_attachment_status,
    ]
    inlines = [FileInlineAdmin]


admin.site.register(Letter, LetterAdmin)
