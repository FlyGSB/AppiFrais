from django.contrib import admin
from .models import *

"""
Permet d'afficher les details des Entite de la Base de Donnee dans
le panneau d'administration Django
"""

# Register your models here.
admin.site.register(FicheFrais)
admin.site.register(Forfait)
admin.site.register(LigneFraisForfait)
admin.site.register(LigneFraisHorsForfait)
admin.site.register(Etat)
admin.site.register(PieceJointe)
