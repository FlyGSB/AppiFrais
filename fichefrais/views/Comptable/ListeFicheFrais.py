from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from fichefrais.forms import FormChoixVisiteur
from fichefrais.models import FicheFrais
from fichefrais.utils import liste_fiche_frais


def liste_fiche_frais_comptable(request):

    choix_visiteur = FormChoixVisiteur(request.POST or None)

    if "visiteur" in request.session:
        id_visiteur = request.session.get("visiteur")
        visiteur = get_object_or_404(User, pk=id_visiteur)
        del request.session["visiteur"]
    elif choix_visiteur.is_valid():
        visiteur = choix_visiteur.cleaned_data.get("visiteur")
    else:
        visiteur = None

    if visiteur:
        qs_fiche_frais = FicheFrais.objects.filter(user=visiteur).order_by("date")
    else:
        qs_fiche_frais = FicheFrais.objects.all().order_by("date")

    fiches_frais = liste_fiche_frais(qs_fiche_frais)

    context = {
        "title": "Archive Fiche Frais",
        "fiches_frais": fiches_frais,
        "choix_visiteur": choix_visiteur,
        "back": request.user.profile.job.home_job,
    }

    return render(request, "fichefrais/comptable/liste_fiche_frais.html", context)
