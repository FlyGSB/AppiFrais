from django.db import models


class Forfait(models.Model):
    libelle_forfait = models.CharField(max_length=50)
    montant = models.FloatField(max_length=6)
    date_debut = models.DateField(auto_now_add=True)
    date_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return "%s: %s€" % (self.libelle_forfait, self.montant)
