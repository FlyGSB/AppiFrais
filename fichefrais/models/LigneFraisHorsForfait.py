from django.db import models
from .FicheFrais import FicheFrais
from .Etat import Etat


class LigneFraisHorsForfait(models.Model):
    fiche_frais = models.ForeignKey(FicheFrais, models.CASCADE)
    etat = models.ForeignKey(Etat)
    montant = models.FloatField(max_length=6)
    libelle_hors_forfait = models.CharField(max_length=40)
    date_frais = models.DateField(editable=True)
    date_ajout = models.DateField(auto_now_add=True)
    date_modification = models.DateField(auto_now=True)

    def __str__(self):
        return "%s - %s€ - %s" % (self.libelle_hors_forfait, self.montant, self.date_ajout)
