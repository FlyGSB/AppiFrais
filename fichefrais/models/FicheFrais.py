from django.contrib.auth.models import User
from django.db import models
from .Etat import Etat


class FicheFrais(models.Model):
    user = models.ForeignKey(User, models.CASCADE, 'fiche_frais')
    etat = models.ForeignKey(Etat, models.SET(0))

    date = models.DateField()
    date_modif = models.DateTimeField(auto_now=True, editable=True)

    nb_justificatif = models.IntegerField()
    montant_valide = models.FloatField(max_length=6)

    def __str__(self):
        return "%s-%s %s" % (self.date.month, self.date.year, self.user)
