from datetime import datetime
from fichefrais.models import Forfait
from fichefrais.utils import decorateur_verification_connexion
from django.shortcuts import render


@decorateur_verification_connexion(utilisateur_autorise=["Comptable"])
def gestion_forfait(request):

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
