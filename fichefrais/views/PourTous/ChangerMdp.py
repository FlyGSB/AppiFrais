from django.shortcuts import render, redirect
from fichefrais.forms.FormChangerMdp import FormChangerMdp


def changer_mdp(request):

    user = request.user
    form_mdp = FormChangerMdp(request.POST or None)

    if form_mdp.is_valid():
        password = form_mdp.cleaned_data.get("password")

        user.set_password(password)
        user.profile.changer_mdp = False
        user.save()
        user.profile.save()
        return redirect("login")

    context = {
        "form_mdp": form_mdp,
        "title": "Création Nouveau Mot de Passe",
    }

    return render(request, "fichefrais/changer_mdp.html", context)
