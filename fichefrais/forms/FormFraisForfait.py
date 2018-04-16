from django import forms
from fichefrais.models import Forfait


class FormFraisForfait(forms.ModelForm):

    class Meta:
        model = Forfait
        fields = ["libelle_forfait", "montant"]
