from django import forms
from .models import TaskGroup

class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = TaskGroup
        fields = ['title', 'description']

class TaskEditForm(forms.ModelForm):
    class Meta:
        model  = TaskGroup
        fields = ['title', 'description', 'done']