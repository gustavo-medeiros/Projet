from django.urls import path
from . import views


urlpatterns = [
    path('projects', views.projects, name='projects'),
    path('connexion', views.connexion, name='connexion'),
    path('deconnexion',views.deconnexion, name='deconnexion'),
]