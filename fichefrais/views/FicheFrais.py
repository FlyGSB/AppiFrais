from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from fichefrais.models import FicheFrais
from fichefrais.utils import liste_fiche_frais


@login_required(login_url="/accounts/login")
def fiche_frais(request, year, month):

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


@login_required(login_url="/accounts/login")
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
