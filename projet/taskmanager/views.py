from django.shortcuts import render, redirect
from .forms import ConnexionForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


def accueil(request):
    return render(request, 'taskmanager/accueil.html')


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
                return redirect(accueil)
            else:  # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()
    return render(request, 'taskmanager/connexion.html', locals())


def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))
