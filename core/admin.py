from django.contrib import admin

from core.models import Appeal


@admin.register(Appeal)
class RoomModels(admin.ModelAdmin):
    list_display = ('id', 'title', 'auditorium' 'status', 'group', 'priority')
    search_fields = ('title', 'auditorium')
    list_filter = ('status', 'group', 'priority')
