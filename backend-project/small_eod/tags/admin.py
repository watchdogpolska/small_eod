from django.contrib import admin

from .models import Tag, TagNamespace

admin.site.register(Tag)
admin.site.register(TagNamespace)
