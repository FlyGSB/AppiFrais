from django.shortcuts import render, redirect
from fichefrais.models import FicheFrais, Etat
from fichefrais.forms import FormLigneFraisForfait, FormLigneFraisHorsForfait
from fichefrais.utils import get_date_fiche_frais


def creation_frais(request):
    """
    :view creation_frais: Permet d'utiliser un formulaire d'ajout de Frais (Forfait, Hors Forfait)
    :template ajout_frais.html:
    """
    title = "Ajouter Frais"

    if request.method == "POST":
        date_fiche_frais = get_date_fiche_frais()
        form_ff = FormLigneFraisForfait(request.POST)
        form_hf = FormLigneFraisHorsForfait(request.POST)
        fiche_frais = FicheFrais.objects.filter(user=request.user, date__year=date_fiche_frais.year,
                                                date__month=date_fiche_frais.month).first()
        etat = Etat.objects.filter(valeur=1).first()

        if form_ff.is_valid():
            ligne_ff = form_ff.save(commit=False)
            ligne_ff.fiche_frais = fiche_frais
            ligne_ff.etat = etat
            ligne_ff.save()
            return redirect(request.user.profile.job.home_job)

        elif form_hf.is_valid():
            ligne_hf = form_hf.save(commit=False)
            ligne_hf.fiche_frais = fiche_frais
            ligne_hf.etat = etat
            ligne_hf.save()
            return redirect(request.user.profile.job.home_job)
    else:
        form_ff = FormLigneFraisForfait()
        form_hf = FormLigneFraisHorsForfait()

    context = {
        "title": title,
        "back": request.user.profile.job.home_job,
        "user": request.user,
        "form_ff": form_ff,
        "form_hf": form_hf,
    }

    return render(request, "fichefrais/visiteur/ajout_frais.html", context)
