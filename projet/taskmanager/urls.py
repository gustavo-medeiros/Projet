from django.urls import path
from . import views


urlpatterns = [
    path('projects', views.projects, name='projects'),
    path('project/<int:project_id>', views.project, name='project'),
    path('task/<int:task_id>', views.task, name='task'),
    path('project/<int:project_id>/newtask', views.newtask, name='newtask'),
    path('connexion', views.connexion, name='connexion'),
    path('deconnexion', views.deconnexion, name='deconnexion'),
]