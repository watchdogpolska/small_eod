from django.contrib import admin

# Register your models here.

from institution.models import Institution, AdministrativeUnit, ExternalIdentifier, AddressData

admin.site.register(Institution)
admin.site.register(AdministrativeUnit)
admin.site.register(ExternalIdentifier)
admin.site.register(AddressData)