from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    Name = models.CharField(max_length=100)
    Members = models.ManyToManyField(User, related_name="projects")

    class Meta:
        verbose_name = "projet"

    def __str__(self):
        return self.Name
