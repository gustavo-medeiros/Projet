from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name="projects")

    class Meta:
        verbose_name = "projet"

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "status"

    def __str__(self):
        return self.name


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    due_date = models.DateField()
    priority = models.PositiveIntegerField()
    status = models.ForeignKey(Status, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "task"

    def __str__(self):
        return self.name


class Journal(models.Model):
    date = models.DateTimeField()
    entry = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "journal"

    def __str__(self):
        return self.entry
