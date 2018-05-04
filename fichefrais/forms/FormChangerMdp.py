from django import forms
from django.contrib.auth.models import User


class FormChangerMdp(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Mot de passe ', required=True)

    class Meta():
        model = User
        fields = ['password']

