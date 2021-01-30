from django.contrib import admin

from .models import Tag


class TagAdmin(admin.ModelAdmin):
    search_fields = ("name",)


admin.site.register(Tag, TagAdmin)
