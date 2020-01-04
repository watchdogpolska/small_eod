from django.contrib import admin

from .models import Institution, AdministrativeUnit, ExternalIdentifier, AddressData


admin.site.register(Institution)
admin.site.register(AdministrativeUnit)
admin.site.register(ExternalIdentifier)
admin.site.register(AddressData)
