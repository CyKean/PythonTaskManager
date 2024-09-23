# Sa iyong forms.py
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']

class TaskStatusForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['completed', 'completed_date']