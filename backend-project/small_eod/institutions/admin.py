from django.contrib import admin

from .models import Institution


class InstitutionAdmin(admin.ModelAdmin):
    search_fields = ["name", "city"]


admin.site.register(Institution, InstitutionAdmin)
