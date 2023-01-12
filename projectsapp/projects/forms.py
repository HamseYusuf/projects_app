from django import forms
from.models import Project
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

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
    


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

