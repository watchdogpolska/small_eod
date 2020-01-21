from rest_framework import serializers
from .models import Letter, Description
from ..generic.serializers import UserLogModelSerializer

from small_eod.files.serializers import FileSerializer


class LetterSerializer(UserLogModelSerializer):
    attachment = FileSerializer(many=True, read_only=True)

    createdOn = serializers.CharField(source='created_on')
    createdBy = serializers.CharField(source='created_by')
    modifiedOn = serializers.CharField(source='modified_on')
    modifiedBy = serializers.CharField(source='modified_by')

    class Meta:
        model = Letter
        fields = [
            "id",
            "name",
            "direction",
            "channel",
            "final",
            "date",
            "identifier",
            "institution",
            "address",
            "case",
            "attachment",
            "ordering",
            "comment",
            "excerpt",
            "createdOn",
            "createdBy",
            "modifiedOn",
            "modifiedBy",
        ]


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = [
            "name",
        ]
