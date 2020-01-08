from django.contrib import admin

from .models import Institution, ExternalIdentifier, AddressData


admin.site.register(Institution)
admin.site.register(ExternalIdentifier)
admin.site.register(AddressData)
