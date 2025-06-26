from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'status',
            'due_date',
        ]
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }
        
        
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter task title'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'rows': 4,
            'placeholder': "Enter task description...",
        })
        self.fields['due_date'].widget.attrs.update({
            'class': 'form-control',
            'type': 'date'
        })
        self.fields['status'].widget.attrs.update({
            'class': 'form-control',
            
        })

class EditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'status',
            'due_date',
        ]
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }
        
    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter task title'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'rows': 4
        })
        self.fields['status'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['due_date'].widget.attrs.update({
            'class': 'form-control',
            'type': 'date'
        })