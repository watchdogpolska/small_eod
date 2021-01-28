from django.contrib import admin
from django.urls import reverse
from django.utils.translation import gettext as _
from django.template.defaultfilters import safe

from .models import Scope, Key


def get_event_ical_link(obj):
    if not obj.scopes.filter(name="export_ical").exists():
        return _("Missing scope 'export_ical'")
    event_url = "{}?token={}".format(reverse("event-ical-list"), obj.token)
    letter_url = "{}?token={}".format(reverse("letter-ical-list"), obj.token)
    return safe(
        _("View calendar for {event_link} or {letter_link}").format(
            event_link='<a href="{}">{}</a>'.format(event_url, _("event")),
            letter_link='<a href="{}">{}</a>'.format(letter_url, _("letter")),
        )
    )


get_event_ical_link.short_description = "Calendar"


class KeyAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "user",
        get_event_ical_link,
        "used_on",
        "created_on",
        "modified_on",
    ]
    exclude = ("token",)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(user=request.user)
        return qs


admin.site.register(Scope)
admin.site.register(Key, KeyAdmin)
