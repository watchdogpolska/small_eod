# app/admin.py

from import_export import resources, widgets
from .models import Institution, Tag


class InstitutionResource(resources.ModelResource):
    tags = resources.Field(
        attribute="tags",
        column_name="tags",
        widget=widgets.ManyToManyWidget(Tag, field="name"),
    )

    class Meta:
        model = Institution
        fields = ["name", "comment", "id"]


class TagResource(resources.ModelResource):
    class Meta:
        model = Tag
        fields = ["name", "id"]
