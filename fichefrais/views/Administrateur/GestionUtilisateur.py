from django.contrib.auth.models import User
from django.shortcuts import render
from datetime import datetime


def gestion_utilisateur(request):
    """
    :view gestion_utilisateur: Vue de gestion de supression + modification des utilisateur
    :template gestion_utilisateur.html:
    """
    today = datetime.today()

    qs_visiteur = User.objects.filter(profile__job__libelle_job__icontains="visiteur")
    qs_comptable = User.objects.filter(profile__job__libelle_job__icontains="comptable")

    context = {
        "title": "Gestion Utilisateur",
        "user": request.user,
        "today": today,
        "visiteur": qs_visiteur,
        "comptable": qs_comptable,
        "action_button_user": "administrateur/action_button_users.html"
    }

    return render(request, "fichefrais/administrateur/gestion_utilisateur.html", context)
