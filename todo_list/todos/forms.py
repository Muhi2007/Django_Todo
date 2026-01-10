from django import forms
from .models import TaskGroup, Todo

class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = TaskGroup
        fields = ['title', 'description']

class TaskEditForm(forms.ModelForm):
    class Meta:
        model  = TaskGroup
        fields = ['title', 'description', 'done']

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'content']

class TodoEditForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'content', 'done']