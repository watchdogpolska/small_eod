from django.db import models
from ..letters.models import Letter


class File(models.Model):
    path = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    letter = models.ForeignKey(to=Letter, on_delete=models.CASCADE, related_name='attachment')
