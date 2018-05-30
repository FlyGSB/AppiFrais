from datetime import datetime
from fichefrais.models import Forfait
from django.shortcuts import render


def gestion_forfait(request):
    """
    :view gestion_forfait: Permet d'afficher la vue de gestion des Forfait
    :template gestion_forfait.html:
    """
    today = datetime.today()
    qs_forfait = Forfait.objects.filter(date_fin=None)

    context = {
        "user": request.user,
        "today": today,
        "liste_forfait": qs_forfait,
        "back": request.user.profile.job.home_job,
        "action_button_forfait": "comptable/action_button_forfait.html"
    }

    return render(request, "fichefrais/comptable/gestion_forfait.html", context)
