from django import forms
from fichefrais.models import LigneFraisHorsForfait


class FormLigneFraisHorsForfait(forms.ModelForm):
    """
    Formulaire de creation d'un Frais hors Forfait
    """
    date_frais = forms.DateField(widget=forms.DateInput({"class": "datepicker", "type": "text"}))

    class Meta:
        model = LigneFraisHorsForfait
        fields = ["libelle_hors_forfait", "montant", "date_frais"]
