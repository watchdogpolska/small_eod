from django.db import models
from ..letters.models import Letter


class File(models.Model):
    letter = models.ForeignKey(to=Letter, on_delete=models.CASCADE)

    path = models.FilePathField()
    name = models.CharField(max_length=100)

