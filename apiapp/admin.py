from django.contrib import admin
from .models import Task, Tag, TaskTag

admin.site.register(Task)
admin.site.register(Tag)
admin.site.register(TaskTag)