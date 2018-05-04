from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(FicheFrais)
admin.site.register(Forfait)
admin.site.register(LigneFraisForfait)
admin.site.register(LigneFraisHorsForfait)
admin.site.register(Etat)
admin.site.register(PieceJointe)
