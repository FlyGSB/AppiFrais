from django.contrib.auth.models import User
from django.db import models

from fichefrais.utils import set_montant_valide


class FicheFrais(models.Model):
    """
    :entity FicheFrais: representation d'une Fiche de Frais
    :field user: Utilisateur lié à la Fiche de Frais
    :field etat: Etat de la fiche de Frais
    :field date: Date pour calculer le mois de la fiche
    :field date_modif: Permet de garder une trace des modifications d'une fiche
    :field nb_justificatif: Nombre de justificatif enregistre pour une fiche
    :field montant_valide: Montant total valide par un Comptable d'une fiche
    """
    user = models.ForeignKey(User, models.CASCADE, 'fiche_frais')
    etat = models.ForeignKey("Etat", models.SET(0))

    date = models.DateField()
    date_modif = models.DateTimeField(auto_now=True, editable=True)

    nb_justificatif = models.IntegerField(default=0)
    montant_valide = models.FloatField(max_length=6, default=0)

    def __str__(self):
        return "%s-%s %s" % (self.date.month, self.date.year, self.user)

    def set_montant_valide(self):
        set_montant_valide(self)
