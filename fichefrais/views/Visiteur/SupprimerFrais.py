from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from fichefrais.utils import get_elem_fiche, decorateur_verification_connexion


@decorateur_verification_connexion(utilisateur_autorise=["Visiteur"])
def supprimer_frais(request, type_elem=None, obj_id=None):

    elem = get_elem_fiche(type_elem, obj_id)

    if elem:
        if elem.fiche_frais.user != request.user:
            return HttpResponseForbidden()
        elem.delete()

    return redirect(request.user.profile.job.home_job)
