from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class TaskGroup(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    done = models.BooleanField(default=False)
    time_create = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author}'s {self.title}" 