from django.db import models


class Forfait(models.Model):
    """
    :entity Forfait: Forfait pour les Frais Forfaitise
    :field libelle_forfait: Libelle du Forfait
    :field montant: Montant du Forfait
    :field date_debut: Date d'ajout
    :field date_fin: Date de fin, permet de garder un ancien forfait pour des anciens Frais
    """
    libelle_forfait = models.CharField(max_length=50)
    montant = models.FloatField(max_length=6)
    date_debut = models.DateField(auto_now_add=True)
    date_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return "%s: %s€" % (self.libelle_forfait, self.montant)
