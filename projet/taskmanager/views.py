from django.shortcuts import render, redirect
from .forms import ConnexionForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import Project


def projects(request):
    "Home page that shows all the projects"
    all_projects = Project.objects.all()  # Nous sélectionnons tous nos projets
    return render(request, 'taskmanager/projects.html', locals())


def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
                return redirect(projects)
            else:  # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()
    return render(request, 'taskmanager/connexion.html', locals())


def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))
