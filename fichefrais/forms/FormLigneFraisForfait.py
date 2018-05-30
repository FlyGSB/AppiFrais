from django import forms
from fichefrais.models import Forfait, LigneFraisForfait


class FormLigneFraisForfait(forms.ModelForm):
    """
    Formulaire de creation d'un Frais Forfaitise
    """
    forfait = forms.ModelChoiceField(queryset=Forfait.objects.filter(date_fin=None), empty_label="Selectionner Forfait")
    quantite = forms.IntegerField()
    date_frais = forms.DateField(widget=forms.DateInput({"class":"datepicker", "type":"text"}))

    class Meta:
        model = LigneFraisForfait
        fields = ["forfait", "quantite", "date_frais"]
