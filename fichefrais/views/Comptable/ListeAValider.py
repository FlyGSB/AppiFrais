from django.shortcuts import render
from datetime import date
from fichefrais.models import FicheFrais
from fichefrais.utils import liste_fiche_frais, ajout_mois


def liste_a_valider(request):
    """
    :view liste_a_valider: permet d'afficher la liste des Fiche de Frais a valider
    :template liste_a_valider.html:
    """
    today = date.today()

    if today.day > 20:
        date_fiche_frais = ajout_mois(today, 1)
        qs_fiche_frais = FicheFrais.objects.filter(date__year=today.year, date__month=date_fiche_frais.month)
    else:
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
