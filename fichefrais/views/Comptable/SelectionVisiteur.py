from datetime import datetime, date
from fichefrais.models import FicheFrais
from django.contrib.auth.models import User
from fichefrais.forms import FormChoixVisiteur
from django.shortcuts import render, get_object_or_404
from fichefrais.utils import liste_fiche_frais, ajout_mois


def selection_visiteur(request):

    title = "Selection Visiteur"
    today = datetime.today()
    choix_visiteur = FormChoixVisiteur(request.POST or None)

    context = {
        "user": request.user,
        "today": today,
        "back": request.user.profile.job.home_job,
        "action_button_frais_forfait": "comptable/action_button_frais_forfait.html",
        "action_button_frais_hors_forfait": "comptable/action_button_frais_hors_forfait.html",
    }

    if "visiteur" in request.session:
        id_visiteur = request.session.get("visiteur")
        visiteur = get_object_or_404(User, pk=id_visiteur)
        del request.session["visiteur"]
    elif choix_visiteur.is_valid():
        visiteur = choix_visiteur.cleaned_data.get("visiteur")
    else:
        visiteur = None

    if visiteur:
        title = "Validation de Frais"
        today = date.today()

        if today.day > 20:
            date_fiche_frais = ajout_mois(today, 1)
            qs_fiche_frais = FicheFrais.objects.filter(user=visiteur, date__year=today.year, date__month=date_fiche_frais.month)
        else:
            qs_fiche_frais = FicheFrais.objects.filter(user=visiteur, date__year=today.year, date__month=today.month)

        if qs_fiche_frais:
            fiche_frais = liste_fiche_frais(qs_fiche_frais)[qs_fiche_frais.first()]
            context["fiche_frais"] = fiche_frais
        else:
            context["message"] = "<p class='red-text'>Aucune fiche de frais trouvé</p>"

    context["title"] = title
    context["choix_visiteur"] = choix_visiteur
    request.session["redirection"] = "selection_visiteur"

    return render(request, "fichefrais/comptable/validation_frais.html", context)
