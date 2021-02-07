from django.contrib import admin

from .models import Key, Scope

admin.register(Scope)
admin.register(Key)
