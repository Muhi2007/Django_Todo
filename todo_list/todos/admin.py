from django.contrib import admin
from .models import TaskGroup, Todo

# Register your models here.
admin.site.register(TaskGroup)
admin.site.register(Todo)