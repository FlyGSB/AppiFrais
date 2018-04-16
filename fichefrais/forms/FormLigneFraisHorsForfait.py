from django import forms
from fichefrais.models import LigneFraisHorsForfait


class FormLigneFraisHorsForfait(forms.ModelForm):

    date_frais = forms.DateField(widget=forms.DateInput({"class": "datepicker", "type": "text"}))

    class Meta:
        model = LigneFraisHorsForfait
        fields = ["libelle_hors_forfait", "montant", "date_frais"]
