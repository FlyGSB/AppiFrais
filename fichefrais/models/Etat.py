from django.db import models


class Etat(models.Model):
    """
    :entity Etat: Etat
    :field libelle: libelle d'un Etat
    :field color: couleur d'affichage du badge
    :field valeur: valeur pour faciliter les requetes
    """
    libelle = models.CharField(max_length=20, null=False)
    color = models.CharField(max_length=20, blank=True)
    valeur = models.IntegerField(name=False)

    def __str__(self):
        return "%s - %s" % (self.valeur, self.libelle)
