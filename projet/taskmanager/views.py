from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ConnexionForm, ChatForm, TaskForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import Project, Task, Journal
from django.utils import timezone


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
    selected_task = get_object_or_404(Task, id=task_id)
    form = ChatForm(request.POST or None)
    if form.is_valid():
        entry = form.cleaned_data['entry']
        Journal(date=timezone.now(), entry=entry, author=request.user, task=selected_task).save()
    entries = Journal.objects.filter(task=selected_task)
    return render(request, 'taskmanager/task.html', locals())


@login_required
def newtask(request, project_id):
    form = TaskForm(request.POST or None)
    selected_project = Project.objects.get(id=project_id)
    form.fields["assignee"].queryset = selected_project.members.all()  # only accepts the envolved members
    if form.is_valid():
        task_to_add = form.save(commit=False)
        task_to_add.project = Project.objects.get(id=project_id)
        task_to_add.save()
        return redirect('task', task_id=task_to_add.id)
    return render(request, 'taskmanager/newtask.html', locals())


@login_required
def edittask(request, task_id):
    selected_task = Task.objects.get(id=task_id)
    form = TaskForm(request.POST or None, instance=selected_task)
    form.fields["assignee"].queryset = Task.objects.get(
        id=task_id).project.members.all()  # only accepts the envolved members
    if form.is_valid():
        form.save()
        return redirect('task', task_id=task_id)
    return render(request, 'taskmanager/newtask.html', locals())  # We use the same template used to create a new task


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
