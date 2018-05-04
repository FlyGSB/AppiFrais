from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from fichefrais.models import LigneFraisForfait


def suppr_ligne_frais_forfait(request, pk):

    ligne_frais_forfait = get_object_or_404(LigneFraisForfait, pk=pk)

    if ligne_frais_forfait:
        if ligne_frais_forfait.fiche_frais.user != request.user:
            return HttpResponseForbidden()
        ligne_frais_forfait.delete()

    return redirect(request.user.profile.job.home_job)
