from django import forms
from.models import Project

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'user',
            'title',
            'category',
            'technology',
            'developers',
            'details',
            'status'
        ]
    



