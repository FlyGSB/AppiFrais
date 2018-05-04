from django.db import models


class LigneFraisForfait(models.Model):
    fiche_frais = models.ForeignKey("FicheFrais", models.CASCADE, 'frais_forfait')
    forfait = models.ForeignKey("Forfait", models.CASCADE, 'forfait')
    etat = models.ForeignKey("Etat")
    quantite = models.IntegerField()
    date_frais = models.DateField(editable=True)
    date_ajout = models.DateField(auto_now_add=True)
    date_modification = models.DateField(auto_now=True)

    @property
    def total(self):
        return self.forfait.montant * self.quantite

    def __str__(self):
        return "%s (%s)" % (self.forfait, self.quantite)
