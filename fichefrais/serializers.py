from django.contrib.auth.models import User
from rest_framework import serializers
from fichefrais.models import FicheFrais, Etat, LigneFraisForfait, LigneFraisHorsForfait, Forfait

###########
# ANDROID #
###########

######################################
# Representation de la Base de Donne #
# pour l'API Android                 #
######################################

class AndroidEtatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etat
        fields = ('valeur', )


class AndroidFicheFraisSerializer(serializers.ModelSerializer):
    etat = serializers.IntegerField(source="etat.valeur")

    class Meta:
        model = FicheFrais
        fields = ('id', 'date', 'montant_valide', 'etat')


class AndroidForfaitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Forfait
        fields = ('libelle_forfait', 'montant',)


class AndroidLigneFraisForfaitSerializer(serializers.ModelSerializer):
    type_f = serializers.CharField(default="frais_forfait", max_length=100)
    libelle = serializers.CharField(source="forfait.libelle_forfait")
    etat = serializers.IntegerField(source="etat.valeur")
    montant = serializers.CharField(source="total")
    date = serializers.CharField(source="date_frais")

    class Meta:
        model = LigneFraisForfait
        fields = ('type_f', 'libelle', 'montant', 'date', 'etat')


class AndroidLigneFraisHorsForfaitSerializer(serializers.ModelSerializer):
    type_f = serializers.CharField(default="frais_hors_forfait", max_length=100)
    libelle = serializers.CharField(source="libelle_hors_forfait")
    etat = serializers.IntegerField(source="etat.valeur")
    date = serializers.CharField(source="date_frais")

    class Meta:
        model = LigneFraisHorsForfait
        fields = ('type_f', 'libelle', 'montant', 'date', 'etat')


class AndroidUserFicheFraisSerializer(serializers.ModelSerializer):
    fiche_frais = AndroidFicheFraisSerializer(many=True)

    class Meta:
        model = User
        fields = ('fiche_frais',)
