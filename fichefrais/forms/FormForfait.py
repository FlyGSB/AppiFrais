from django import forms
from fichefrais.models import Forfait


class FormForfait(forms.ModelForm):
    """
    Formulaire de creation d'un Forfait
    """
    class Meta:
        model = Forfait
        fields = ["libelle_forfait", "montant"]
