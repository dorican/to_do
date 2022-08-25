from django.contrib import admin

from backend.todo.models import Project, ToDo


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', )


@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('project', 'user')
    search_fields = ('project', 'user')
    autocomplete_fields = ('project', 'user')
