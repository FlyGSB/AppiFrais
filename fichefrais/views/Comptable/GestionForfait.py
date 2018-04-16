from datetime import datetime
from fichefrais.models import Forfait
from fichefrais.utils import verify_connexion_decorator
from django.shortcuts import render


@verify_connexion_decorator(utilisateur_autorise=["Comptable"])
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
