from django.contrib import admin
from django.contrib.auth import get_user_model


class UserAdmin(admin.ModelAdmin):
    search_fields = ["username", "official_name"]


User = get_user_model()

admin.site.register(User, UserAdmin)
