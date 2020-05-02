from django import forms
from .models import Task


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


class ChatForm(forms.Form):
    entry = forms.CharField(label="New entry")


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ('project',)
