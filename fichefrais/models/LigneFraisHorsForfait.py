from django.db import models


class LigneFraisHorsForfait(models.Model):
    """
    :entity LigneFraisHorsForfait: Frais hors forfait
    :field fiche_frais: Fiche Frais attache au Frais
    :field etat: Etat du Frais
    :field montant: Montant du Frais
    :field libelle_hors_forfait: Libelle du Frais
    :field date_frais: Date d'aquisition du Frais
    :field date_ajout: Data de l'ajout sur l'application
    :field date_modification: Date de dernière modification du Frais
    """
    fiche_frais = models.ForeignKey("FicheFrais", models.CASCADE, "frais_hors_forfait")
    etat = models.ForeignKey("Etat")
    montant = models.FloatField(max_length=6)
    libelle_hors_forfait = models.CharField(max_length=40)
    date_frais = models.DateField(editable=True)
    date_ajout = models.DateField(auto_now_add=True)
    date_modification = models.DateField(auto_now=True)

    @property
    def total(self):
        return self.montant

    def __str__(self):
        return "%s - %s€ - %s" % (self.libelle_hors_forfait, self.montant, self.date_ajout)
