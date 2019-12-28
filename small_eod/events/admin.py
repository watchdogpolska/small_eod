from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.EventType)
class EventTypeAdmin(admin.ModelAdmin): ...

@admin.register(models.CaseEvent)
class CaseEventAdmin(admin.ModelAdmin): ...
