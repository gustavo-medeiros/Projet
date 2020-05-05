from django import forms
from .models import Task


class ConnexionForm(forms.Form):  # used in login
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


class ChatForm(forms.Form):  # used in the journal
    entry = forms.CharField(label="New entry")


class TaskForm(forms.ModelForm):  # based on the model Form; used in newtask and edittask
    class Meta:
        model = Task
        exclude = ('project',)  # the project will be the one the user is adding the project to (or the one that exists already)
