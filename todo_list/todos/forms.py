from django import forms
from .models import Task

class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']

class TaskEditForm(forms.ModelForm):
    class Meta:
        model  = Task
        fields = ['title', 'description', 'done']