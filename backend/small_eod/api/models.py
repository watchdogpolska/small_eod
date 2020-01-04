from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from generic.models import TimestampUserLogModel


class TagNamespace(TimestampUserLogModel):
    description = models.CharField(max_length=256)
    color = models.CharField(max_length=9, default='0000000000')


class Tag(models.Model):
    limit = models.Q(app_label='case', model='Case') | models.Q(app_label='api', model='Letter')

    tag_field = models.CharField(max_length=256)
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to= limit
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


