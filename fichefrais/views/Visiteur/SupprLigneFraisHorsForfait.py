from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from fichefrais.models import LigneFraisHorsForfait


def suppr_ligne_frais_hors_forfait(request, pk):
    """
    :view suppr_ligne_frais_hors_forfait: permet de supprimer un Frais Hors Forfait d'une Fiche de Frais
    :param pk: clef primaire d'un Frais Hors Forfait
    :return: redirige vers l'accueil de l'utilisateur
    """
    ligne_frais_hors_forfait = get_object_or_404(LigneFraisHorsForfait, pk=pk)

    if ligne_frais_hors_forfait:
        if ligne_frais_hors_forfait.fiche_frais.user != request.user:
            return HttpResponseForbidden()
        ligne_frais_hors_forfait.delete()

    return redirect(request.user.profile.job.home_job)
