from django.shortcuts import render
from fichefrais.utils import decorateur_verification_connexion
from fichefrais.models import Forfait
from datetime import datetime


@decorateur_verification_connexion(utilisateur_autorise=["Comptable"])
def liste_ancien_forfait(request):

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