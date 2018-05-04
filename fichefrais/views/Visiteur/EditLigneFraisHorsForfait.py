from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect

from fichefrais.forms import FormLigneFraisHorsForfait
from fichefrais.models import LigneFraisHorsForfait, Etat
from fichefrais.utils import get_date_fiche_frais


def edit_ligne_frais_hors_forfait(request, pk):

    ligne_frais_hors_forfait = get_object_or_404(LigneFraisHorsForfait, pk=pk)
    date_fiche_frais = get_date_fiche_frais()

    if ligne_frais_hors_forfait.fiche_frais.user != request.user:
        return HttpResponseForbidden()
    elif ligne_frais_hors_forfait.fiche_frais.date.month != date_fiche_frais.month or ligne_frais_hors_forfait.fiche_frais.date.year != date_fiche_frais.year:
        return HttpResponseForbidden()

    edit_form = FormLigneFraisHorsForfait(request.POST or None, instance=ligne_frais_hors_forfait)

    if edit_form.is_valid():
        ligne_frais_hors_forfait = edit_form.save(commit=False)
        ligne_frais_hors_forfait.etat = Etat.objects.get(valeur=1)
        ligne_frais_hors_forfait.save()
        ligne_frais_hors_forfait.fiche_frais.set_montant_valide()
        return redirect(request.user.profile.job.home_job)

    context = {
        "edit_form": edit_form,
        "element": "Frais Hors Forfait",
        "back": request.user.profile.job.home_job,
    }

    return render(request, "fichefrais/edition_elem_fiche_frais.html", context)
