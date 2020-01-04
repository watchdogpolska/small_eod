from django.db import models
from letter.models import Letter


class File(models.Model):
    path = models.FilePathField()
    name = models.CharField(max_length=100)
    letter = models.ForeignKey(to=Letter, on_delete=models.CASCADE)

