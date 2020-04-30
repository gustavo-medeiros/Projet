from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ConnexionForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import Project


@login_required
def projects(request):
    # Home page that shows all the projects of the connected user
    user_projects = request.user.projects.all()  # Nous sélectionnons tous nos projets du utilisateur
    return render(request, 'taskmanager/projects.html', locals())


@login_required
def project(request, project_id):
    selected_project = get_object_or_404(Project, id=project_id)
    return render(request, 'taskmanager/project.html', locals())


@login_required
def task(request, task_id):
    selected_task = get_object_or_404(Project, id=task_id)
    return render(request, 'taskmanager/task.html', locals())


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
