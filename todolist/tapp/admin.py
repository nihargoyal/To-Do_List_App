from django.contrib import admin
from .models import Todo, Tag
# Register your models here.

# admin.site.register(Todo)
# admin.site.register(Tag)

@admin.register(Todo)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'duedate', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'description')
    readonly_fields = ('timestamp',)
    fieldsets = (
        ('Task Details', {
            'fields': ('title', 'description', 'duedate', 'status')
        }),
        ('Tags', {
            'fields': ('tag',)
        }),
    )
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
