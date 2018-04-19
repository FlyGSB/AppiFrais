from django.shortcuts import render
from fichefrais.models import FicheFrais
from fichefrais.utils import liste_fiche_frais, decorateur_verification_connexion


@decorateur_verification_connexion(utilisateur_autorise=["Visiteur"])
def list_fiche_frais(request):

    title = "Liste Fiche De Frais"

    qs_fiche_frais = FicheFrais.objects.filter(user=request.user).all()
    fiches_frais = liste_fiche_frais(qs_fiche_frais)

    context = {
        "title": title,
        "back": request.user.profile.job.home_job,
        "fiches_frais": fiches_frais,
    }

    return render(request, "fichefrais/visiteur/liste_fiche_frais.html", context)
