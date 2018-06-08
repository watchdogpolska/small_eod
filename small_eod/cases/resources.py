# app/admin.py

from import_export import resources
from .models import Institution


class InstitutionResource(resources.ModelResource):

    class Meta:
        model = Institution
