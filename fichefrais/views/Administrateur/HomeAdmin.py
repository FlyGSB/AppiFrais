from django.shortcuts import render, redirect
from datetime import datetime
from fichefrais.models import  FicheFrais, Etat, LigneFraisForfait, LigneFraisHorsForfait, Forfait


def home_admin(request):
    """
    :view home_admin: Menu principale des Administrateurs
    :template home_admin.html:
    """
    if not request.user.is_authenticated():
        return redirect("login")

    title = "Accueil"
    today = datetime.now()

    etat = Etat.objects
    fiche_frais = FicheFrais.objects
    frais_forfait = Forfait.objects
    lignes_frais_forfait = LigneFraisForfait.objects
    lignes_frais_hors_forfait = LigneFraisHorsForfait.objects

    context = {
        "title": title,
        "user": request.user,
        "fiche_frais": fiche_frais,
        "lignes_frais_forfait": lignes_frais_forfait,
        "lignes_frais_hors_forfait": lignes_frais_hors_forfait,
        "etat": etat,
        "today": today,
        "frais_forfait": frais_forfait,
    }

    return render(request, "fichefrais/administrateur/home_admin.html", context)
