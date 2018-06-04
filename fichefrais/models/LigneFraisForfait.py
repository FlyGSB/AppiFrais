from django.db import models


class LigneFraisForfait(models.Model):
    """
    :entity LigneFraisForfait: Frais forfaitise
    :field fiche_frais: Fiche Frais attache au Frais
    :field forfait: Forfait utilise pour le Frais
    :field etat: Etat du Frais
    :field quantite: Quantite du Frais utilise
    :field date_frais: Date d'aquisition du Frais
    :field date_ajout: Data de l'ajout sur l'application
    :field date_modification: Date de dernière modification du Frais
    """
    fiche_frais = models.ForeignKey("FicheFrais", models.CASCADE, 'frais_forfait')
    forfait = models.ForeignKey("Forfait", models.CASCADE, 'forfait')
    etat = models.ForeignKey("Etat")
    quantite = models.IntegerField()
    date_frais = models.DateField(editable=True)
    date_ajout = models.DateField(auto_now_add=True)
    date_modification = models.DateField(auto_now=True)

    @property
    def total(self):
        return round(self.forfait.montant * self.quantite, 2)

    def __str__(self):
        return "%s (%s)" % (self.forfait, self.quantite)
