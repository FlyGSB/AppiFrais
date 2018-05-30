from django import forms
from django.contrib.auth.models import User


class FormChoixVisiteur(forms.Form):
    """
    Formulaire: liste déroulante de choix d'un utilisateur ou le job = Visiteur
    """
    visiteurs_query = User.objects.filter(profile__job__valeur_job=1)
    visiteur = forms.ModelChoiceField(queryset=visiteurs_query, empty_label="Choisir un Visiteur", widget=forms.Select(attrs={'onChange': 'this.form.submit();'}))
