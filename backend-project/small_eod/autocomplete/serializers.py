from rest_framework import serializers

from ..administrative_units.models import AdministrativeUnit
from ..cases.models import Case, Tag
from ..channels.models import Channel
from ..features.models import Feature, FeatureOption
from ..institutions.models import Institution
from ..letters.models import DocumentType
from ..users.models import User


class AdministrativeUnitAutocompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdministrativeUnit
        fields = ["id", "name"]


class CaseAutocompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = ["id", "name"]


class ChannelAutocompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ["id", "name"]


class DocumentTypeAutocompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = ["id", "name"]


class FeatureAutocompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ["id", "name"]


class FeatureOptionAutocompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureOption
        fields = ["id", "name"]


class InstitutionAutocompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ["id", "name"]


class TagAutocompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class UserAutocompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]
