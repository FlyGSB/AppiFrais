from django import forms
from .models import Profile, Job
from django.contrib.auth import (
    authenticate,
    get_user_model,
)

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Nom d\'utilisateur ')
    password = forms.CharField(widget=forms.PasswordInput(),label='Mot de passe ')

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError("L'utilisateur n'existe pas")

            if not user.check_password(password):
                raise forms.ValidationError("Mot de passe incorrect")

            if not user.is_active:
                raise forms.ValidationError("Cet utilisateur n'est pas activé")

        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput,label='Mot de passe ', required=True)
    first_name = forms.CharField(label='Prenom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse E-Mail', required=True)


    class Meta():
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']

    def clean_email_conf(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        return email

class ProfileRegisterForm(forms.ModelForm):

    adresse = forms.CharField(label='Adresse ')
    ville = forms.CharField(label='Ville ')
    cp = forms.CharField(label='Code Postal ')
    job = forms.ModelChoiceField(queryset= Job.objects,label='Poste ', empty_label= "Sélectionner un poste", required=True)

    class Meta:
        model = Profile
        fields = ["adresse", "ville", "cp", "job"]

    def save(self, user):
        profile = Profile.objects.create(user=user, adresse=self.cleaned_data.get("adresse"), ville=self.cleaned_data.get("ville"), cp=self.cleaned_data.get("cp"), job=self.cleaned_data.get("job"))
        return profile
