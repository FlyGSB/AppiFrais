from django.shortcuts import redirect, render
from django.http import HttpResponseForbidden
from fichefrais.models import LigneFraisForfait, LigneFraisHorsForfait, Forfait
from fichefrais.forms import FormLigneFraisForfait, FormLigneFraisHorsForfait, FormFraisForfait
from fichefrais.utils import get_elem_fiche, verification_connexion, get_date_fiche_frais


def edit_elem_fiche_frais(request, type_elem=None, obj_id=None):

    elem = get_elem_fiche(type_elem, obj_id)
    date_fiche_frais = get_date_fiche_frais()

    if isinstance(elem, LigneFraisForfait):
        connexion = verification_connexion(request, ["visiteur"])
        if connexion:
            return connexion
        if elem.fiche_frais.user != request.user:
            return HttpResponseForbidden()
        elif elem.fiche_frais.date.month != date_fiche_frais.month or elem.fiche_frais.date.year != date_fiche_frais.year:
            return HttpResponseForbidden()
        nom_obj = "Frais Forfaitisé"
        edit_form = FormLigneFraisForfait(request.POST or None, instance=elem)

    elif isinstance(elem, LigneFraisHorsForfait):
        connexion = verification_connexion(request, ["visiteur"])
        if connexion:
            return connexion
        if elem.fiche_frais.user != request.user:
            return HttpResponseForbidden()
        elif elem.fiche_frais.date.month != date_fiche_frais.month or elem.fiche_frais.date.year != date_fiche_frais.year:
            return HttpResponseForbidden()
        nom_obj = "Frais Hors Forfait"
        edit_form = FormLigneFraisHorsForfait(request.POST or None, instance=elem)

    elif isinstance(elem, Forfait):
        connexion = verification_connexion(request, ["comptable"])
        if connexion:
            return connexion
        nom_obj = "Forfait"
        edit_form = FormFraisForfait(request.POST or None, instance=elem)
    else:
        return redirect(request.user.profile.job.home_job)

    if edit_form.is_valid():
        edit_form.save()
        return redirect(request.user.profile.job.home_job)

    context = {
        "edit_form": edit_form,
        "element": nom_obj,
        "back": request.user.profile.job.home_job,
    }

    return render(request, "fichefrais/edition_elem_fiche_frais.html", context)
