from django.shortcuts import render
from datetime import date
from fichefrais.models import FicheFrais
from fichefrais.utils import get_temps_relatif, ajout_mois


def home_comptable(request):

    title = "Accueil"
    today = date.today()
    end = date(today.year, today.month, 20)
    campagne = False

    if today.day >= 10 and today.day <= 20:
        campagne = True

    if today.day > 20:
        date_fiche_frais = ajout_mois(today, 1)
        left = get_temps_relatif(ajout_mois(end, 1), today)
        nb_fiche_frais = FicheFrais.objects.filter(date__year=today.year, date__month=date_fiche_frais.month,
                                                   etat__valeur=1).count()
    else:
        date_fiche_frais = today
        left = get_temps_relatif(end, today)
        nb_fiche_frais = FicheFrais.objects.filter(date__year=today.year, date__month=today.month,
                                                   etat__valeur=1).count()

    context = {
        "title": title,
        "left": left,
        "campagne": campagne,
        "date_fiche_frais": date_fiche_frais,
        "nb_fiche_frais": nb_fiche_frais
    }

    return render(request, "fichefrais/comptable/home_comptable.html", context)
