from django.shortcuts import render
from fichefrais.models import Forfait
from datetime import datetime


def liste_ancien_forfait(request):
    """
    :view liste_ancien_forfait: permet d'afficher la liste des Forfait cloture
    :template gestion_forfait.html:
    """
    today = datetime.today()
    qs_forfait = Forfait.objects.filter(date_fin__lte=today)

    context = {
        "user":request.user,
        "title": "Ancien Forfait",
        "today": today,
        "liste_forfait": qs_forfait,
        "back": request.user.profile.job.home_job
    }

    return render(request, "fichefrais/comptable/gestion_forfait.html", context)
