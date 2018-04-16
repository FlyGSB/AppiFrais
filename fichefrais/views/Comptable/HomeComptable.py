from django.shortcuts import render
from datetime import datetime
from fichefrais.models import FicheFrais
from fichefrais.utils import verify_connexion_decorator


@verify_connexion_decorator(utilisateur_autorise=["Comptable", "Administrateur"])
def home_comptable(request):

    title = "Accueil"
    today = datetime.today()
    start = datetime(today.year, today.month, 10)
    end = datetime(today.year, today.month, 20)
    left = end - today

    if (today.day >= start.day) and (today.day <= end.day):
        etat_bouton_vistiteur = ""
        new_fiche_frais = len(FicheFrais.objects.filter(date__year=today.year, date__month=today.month, etat__valeur=1))
    else:
        etat_bouton_vistiteur = "disabled"
        new_fiche_frais = ""

    context = {
        "title": title,
        "left": left.days+1,
        "new_fiche": new_fiche_frais,
        "etat_boutton": etat_bouton_vistiteur,
    }

    return render(request, "fichefrais/comptable/home_comptable.html", context)
