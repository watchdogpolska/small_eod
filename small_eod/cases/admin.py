import unicodedata
from os.path import basename

import zipstream as zipstream
from django.contrib import admin
from django.db import models
from django.forms import widgets
from django.http import StreamingHttpResponse
from django.template.defaultfilters import safe
from django.urls import reverse
from django.utils.encoding import force_text
from django.utils.html import escape
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportMixin
from small_eod.events.models import Event
from small_eod.cases.models import (
    Letter,
    Institution,
    Case,
    Channel,
    Tag,
    Person,
    Dictionary,
    LetterName,
)
from small_eod.cases.resources import InstitutionResource, TagResource


def display_tags(obj):
    return ", ".join(force_text(x) for x in obj.tags.all()) or "-"


display_tags.short_description = _("Tags")


def link_to_letters(obj):
    url = reverse("admin:cases_letter_changelist") + "?case__id__exact=" + str(obj.pk)
    return safe(
        '<a href="{}">{}</a>'.format(url, _("View {} letters").format(obj.letter_count))
    )


link_to_letters.short_description = _("Letters")


def link_to_case(obj):
    if not obj.case_id:
        return None
    url = reverse("admin:cases_case_changelist") + "?pk__exact=" + str(obj.case_id)
    return safe('<a href="{}">{}</a>'.format(url, escape(obj.case)))


link_to_case.short_description = _("Case")


def get_attachment_status(obj):
    return bool(obj.attachment)


get_attachment_status.short_description = _("Attachment")
get_attachment_status.boolean = True


class LetterInline(admin.StackedInline):
    sortable_field_name = "ordering"
    model = Letter
    extra = 0
    raw_id_fields = [
        "institution",
    ]

    autocomplete_lookup_fields = {
        "fk": [
            "institution",
        ]
    }


class EventInline(admin.StackedInline):
    model = Event
    extra = 0


class InstitutionTagFilter(admin.RelatedOnlyFieldListFilter):
    def __init__(self, field, request, params, model, model_admin, field_path):
        super().__init__(field, request, params, model, model_admin, field_path)
        self.title = _("Institution tags by letters")


def download_selected_letters(modeladmin, request, queryset):
    z = zipstream.ZipFile()
    for letter in queryset.filter(attachment__isnull=False).select_related("case"):
        case_name = letter.case.name if letter.case else "unknown"
        case_name = unicodedata.normalize("NFKD", case_name.replace("/", "__"))
        z.write(
            letter.attachment.path,
            "{case_id}-{case_name}/{ordering}-{filename}".format(
                case_id=letter.case.id or "unknown",
                case_name=case_name,
                ordering=letter.ordering,
                filename=basename(letter.attachment.path),
            ),
        )
    response = StreamingHttpResponse(
        streaming_content=z,
        content_type="application/zip",
    )
    response["Content-Disposition"] = 'attachment; filename="letters.zip"'
    return response


download_selected_letters.short_description = _("Download selected letters")


class CaseAdmin(admin.ModelAdmin):
    inlines = [LetterInline, EventInline]
    list_display = [
        "name",
        "audited_institution",
        "comment",
        "created",
        "modified",
        display_tags,
        link_to_letters,
    ]
    list_filter = [
        "responsible_people",
        "tags",
        "audited_institution",
        "whose_case",
        "what_scope",
        "inaction_scope",
        "decision_scope",
        "time_of_info_provide",
        "proceddings_interrupted",
        "status",
    ]
    search_fields = ["name", "comment", "audited_institution__name", "comment"]

    raw_id_fields = ["responsible_people", "audited_institution", "tags"]

    formfield_overrides = {
        models.ManyToManyField: {"widget": widgets.CheckboxSelectMultiple},
    }

    autocomplete_lookup_fields = {
        "fk": [
            "audited_institution",
        ],
        "m2m": ["responsible_people", "tags"],
    }

    def get_queryset(self, request):
        return (
            super()
            .get_queryset(request)
            .annotate(letter_count=models.Count("letter"))
            .select_related("audited_institution")
            .prefetch_related("tags")
        )

    link_to_letters.admin_order_field = "letter_count"


class InstitutionAdmin(ImportExportMixin, admin.ModelAdmin):
    raw_id_fields = ["tags"]
    list_display = ["name", "comment", "created", "modified", display_tags]
    search_fields = ["name", "comment"]

    resource_class = InstitutionResource

    autocomplete_lookup_fields = {
        "m2m": ["tags"],
    }


class LetterAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "name",
        "direction",
        "institution",
        "data",
        "identifier",
        link_to_case,
        "comment",
        "created",
        "modified",
        "channel",
        get_attachment_status,
    ]
    list_filter = ["institution", "name", "direction", "case", "channel"]
    search_fields = [
        "name__content",
        "comment",
        "identifier",
        "institution__name",
        "comment",
        "case__name",
    ]
    actions = [download_selected_letters]
    raw_id_fields = ["institution", "case"]

    autocomplete_lookup_fields = {
        "fk": ["institution", "case"],
    }

    def get_queryset(self, request):
        return (
            super()
            .get_queryset(request)
            .select_related("channel", "channel", "institution", "case", "name")
        )


class TagAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = TagResource


class PersonAdmin(admin.ModelAdmin):
    list_display = ["name", "user"]


admin.site.register(Person, PersonAdmin)
admin.site.register(Dictionary)
admin.site.register(Tag, TagAdmin)
admin.site.register(Channel)
admin.site.register(Case, CaseAdmin)
admin.site.register(LetterName)
admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Letter, LetterAdmin)
