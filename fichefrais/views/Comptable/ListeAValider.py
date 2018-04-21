from django.shortcuts import render
from datetime import datetime
from fichefrais.models import FicheFrais
from fichefrais.utils import liste_fiche_frais


def liste_a_valider(request):

    today = datetime.today()
    qs_fiche_frais = FicheFrais.objects.filter(date__year=today.year, date__month=today.month)
    fiches_frais = liste_fiche_frais(qs_fiche_frais)

    context = {
        "user": request.user,
        "title": "Liste Fiche à Valider",
        "today": today,
        "fiches_frais": fiches_frais,
        "back": request.user.profile.job.home_job,
        "action_button_frais_forfait": "comptable/action_button_frais_forfait.html",
        "action_button_frais_hors_forfait": "comptable/action_button_frais_hors_forfait.html",
    }
    request.session["redirection"] = "liste_validation"

    return render(request, "fichefrais/comptable/liste_a_valider.html", context)
