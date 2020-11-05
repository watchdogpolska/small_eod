from django.contrib import admin

from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ["date", "name", "case", "created_on", "modified_on"]
    search_fields = ["name", "comment"]
    list_filter = ["case"]
    raw_id_fields = ["case"]
    autocomplete_lookup_fields = {"fk": ["case"]}


admin.site.register(Event, EventAdmin)
