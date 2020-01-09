from rest_framework import serializers
from django.db import models
from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    choices = ((models.Q(app_label='cases', model='Case'), 'Case'), (models.Q(app_label='letter', model='Letter'), 'Letter'))

    content_type = serializers.ChoiceField(choices=choices)
    class Meta:
        model = Tag
        fields = ['tag_string', 'object_id', 'content_type', ]
