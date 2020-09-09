from django.contrib import admin

from .models import Letter, DocumentType


admin.site.register(Letter)
admin.site.register(DocumentType)
