from django import forms
from .models import Task, Tag, TaskTag

class TaskForm(forms.ModelForm):
    class Meta: 
        model = Task
        fields = ['title', 'description', 'due_date', 'is_done']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

class TaskTagForm(forms.ModelForm):
    class Meta:
        model = TaskTag
        fields = ['task', 'tag']

