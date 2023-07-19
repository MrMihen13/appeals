from django.contrib import admin

from cauth import models


@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active')
    list_filter = ('is_active', 'is_superuser')
    search_fields = ('email', )
