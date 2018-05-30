from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from fichefrais.models import FicheFrais
from fichefrais.utils import liste_fiche_frais


def fiche_frais(request, year, month):
    """
    :view fiche_frais: permet d'afficher les detail d'une Fiche de Frais
    :param year: annee de la Fiche de Frais
    :param month: mois de la Fiche de Frais
    :template fiche_frais_detail.html:
    """
    qs_fiche_frais = FicheFrais.objects.filter(user=request.user, date__year=year, date__month=month)

    if len(qs_fiche_frais) > 0:
        fiche_frais = liste_fiche_frais(qs_fiche_frais)[qs_fiche_frais[0]]
    else:
        return redirect("/")

    context = {
        "title": "Fiche de frais (%s/%s)" % (qs_fiche_frais[0].date.month, qs_fiche_frais[0].date.year),
        "fiche_frais": fiche_frais
    }

    return render(request, "fichefrais/fiche_frais_detail.html", context)


def user_fiche_frais(request, id_user, year, month):

    user = User.objects.filter(id=id_user).first()
    qs_fiche_frais = FicheFrais.objects.filter(user=user, date__year=year, date__month=month)

    if len(qs_fiche_frais) > 0:
        fiche_frais = liste_fiche_frais(qs_fiche_frais)[qs_fiche_frais[0]]
    else:
        return redirect("/")

    mois = qs_fiche_frais[0].date.month
    annee = qs_fiche_frais[0].date.year
    name = user.username

    context = {
        "title": "Fiche de frais (%s/%s) de %s" % (mois, annee, name),
        "fiche_frais": fiche_frais
    }

    return render(request, "fichefrais/fiche_frais_detail.html", context)
