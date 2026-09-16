from django import forms
from .models import Task, Tag, TaskTag

class TaskForm(forms.ModelForm):
        model = Task
        fields = ['title', 'description', 'due_date', 'is_done']

class TagForm(forms.ModelForm):
        model = Tag
        fields = ['name']

class TaskTagForm(forms.ModelForm):
        model = TaskTag
        fields = ['task', 'tag']

