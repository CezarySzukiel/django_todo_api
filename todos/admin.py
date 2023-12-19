from django.contrib import admin
from . import models


class TodoAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'body'
    )


admin.site.register(models.Todo, TodoAdmin)
