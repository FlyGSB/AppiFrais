from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from fichefrais.models import PieceJointe, FicheFrais


def suppr_justificatif(request, pk):

    justificatif = get_object_or_404(PieceJointe, pk=pk)

    if justificatif:
        if justificatif.fiche_frais.user != request.user:
            return HttpResponseForbidden()
        fiche_frais = FicheFrais.objects.get(id=justificatif.fiche_frais.id)
        fiche_frais.nb_justificatif -= 1
        fiche_frais.save()
        justificatif.delete()

    return redirect(request.user.profile.job.home_job)
