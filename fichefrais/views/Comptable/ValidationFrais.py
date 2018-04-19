from django.shortcuts import redirect
from fichefrais.models import Etat
from fichefrais.utils import get_elem_fiche, decorateur_verification_connexion


@decorateur_verification_connexion(utilisateur_autorise=["Comptable"])
def validation_frais(request, valide=None, type_frais=None, frais_id=None):

    if valide:
        frais = get_elem_fiche(type_frais, frais_id)

        if frais:
            fiche_frais = frais.fiche_frais
            etat = Etat.objects.filter(valeur=int(valide)).first()
            etat_fiche = Etat.objects.filter(valeur=7).first()

            if fiche_frais.etat != etat_fiche:
                fiche_frais.etat = etat_fiche
                fiche_frais.save()

            frais.etat = etat
            frais.save()
            request.session["visiteur"] = frais.fiche_frais.user.id

    if "redirection" in request.session:
        return redirect(request.session["redirection"])

    return redirect(request.user.profile.job.home_job)
