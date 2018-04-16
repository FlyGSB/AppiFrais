from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):
    libelle_job = models.CharField(max_length=15, null=False)
    valeur_job = models.IntegerField(name=False)
    home_job = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.libelle_job


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adresse = models.CharField(max_length=40, blank=True)
    ville = models.CharField(max_length=40, blank=True)
    cp = models.CharField(max_length=5, blank=True)
    # job = models.CharField(max_length=20, null=False)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, blank=True)
