from django.shortcuts import render
from datetime import datetime
from fichefrais.utils import decorateur_verification_connexion
from django.contrib.auth.models import User


@decorateur_verification_connexion(utilisateur_autorise=["Administrateur"])
def liste_user(request):

    today = datetime.today()
    qs_user = User.objects.all()

    context = {
        "user": request.user,
        "title": "Liste Utilisateur",
        "today": today,
        "qs_user": qs_user,
        "back": request.user.profile.job.home_job,
    }

    return render(request, "fichefrais/administrateur/liste_user.html", context)
