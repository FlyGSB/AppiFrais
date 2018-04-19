import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from fichefrais.models import FicheFrais, Etat
from fichefrais.utils import (liste_fiche_frais, decorateur_verification_connexion,
                              get_date_fiche_frais, get_date_fin_fiche_frais, get_temps_relatif)


@login_required(login_url="/accounts/login")
@decorateur_verification_connexion(utilisateur_autorise=["Visiteur"])
def home_visiteur(request):

    title = "Accueil"
    today = datetime.date.today()

    date_fiche_frais = get_date_fiche_frais()
    date_fin_fiche_frais = get_date_fin_fiche_frais()

    qs_fiche_frais = FicheFrais.objects.filter(user=request.user, date__month=date_fiche_frais.month,
                                               date__year=date_fiche_frais.year)

    left = get_temps_relatif(date_fin_fiche_frais, today)

    if not qs_fiche_frais:
        etat = Etat.objects.filter(valeur=1).first()
        qs_fiche_frais = [FicheFrais.objects.create(user=request.user, etat=etat,
                                                    nb_justificatif=0, montant_valide=0, date=date_fiche_frais)]

    fiche_frais = liste_fiche_frais(qs_fiche_frais)[qs_fiche_frais[0]]

    context = {
        "title": title,
        "left": left,
        "fiche_frais": fiche_frais,
        "date_fiche_frais": date_fiche_frais,
        "action_button_frais_forfait": "visiteur/action_button_frais_forfait.html",
        "action_button_frais_hors_forfait": "visiteur/action_button_frais_hors_forfait.html",
        "action_button_justificatif": "visiteur/action_button_justificatif.html",
    }

    return render(request, "fichefrais/visiteur/home_visiteur.html", context)
