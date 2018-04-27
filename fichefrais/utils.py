import datetime
import calendar
from dateutil.relativedelta import relativedelta
from django.shortcuts import get_object_or_404, redirect


def liste_fiche_frais(qs_fiche_frais):
    from fichefrais.models import LigneFraisForfait, LigneFraisHorsForfait, PiecesJointe
    fiches_frais = {}
    for fiche in qs_fiche_frais:
        frais_forfait = LigneFraisForfait.objects.filter(fiche_frais=fiche)
        frais_hors_forfait = LigneFraisHorsForfait.objects.filter(fiche_frais=fiche)
        justificatif = PiecesJointe.objects.filter(fiche_frais=fiche)
        sous_total_frais_forfait = sum([ligne.total for ligne in frais_forfait])
        sous_total_frais_hors_forfait = sum([ligne.montant for ligne in frais_hors_forfait])
        etat_fiche_frais = fiche.etat
        fiches_frais[fiche] = {
            "user": fiche.user,
            "etat": etat_fiche_frais,
            "lignes_frais_forfait": frais_forfait,
            "lignes_frais_hors_forfait": frais_hors_forfait,
            "justificatif": justificatif,
            "sous_total_frais_forfait": sous_total_frais_forfait,
            "sous_total_frais_hors_forfait": sous_total_frais_hors_forfait,
            "total": round(sous_total_frais_forfait + sous_total_frais_hors_forfait, 2),
        }
    return fiches_frais


def get_elem_fiche(type_elem=None, obj_id=None):
    from fichefrais.models import LigneFraisForfait, LigneFraisHorsForfait, PiecesJointe, Forfait
    elem = None

    if obj_id and type_elem:
        if type_elem == "frais_forfait":
            elem = get_object_or_404(LigneFraisForfait, pk=obj_id)
        elif type_elem == "frais_hors_forfait":
            elem = get_object_or_404(LigneFraisHorsForfait, pk=obj_id)
        elif type_elem == "justificatif":
            elem = get_object_or_404(PiecesJointe, pk=obj_id)
        elif type_elem == "forfait":
            elem = get_object_or_404(Forfait, pk=obj_id)
    return elem


def get_default_context(request=None, title=""):
    context = {}
    today = datetime.datetime.today()

    if request:
        if request.user:
            context["user"] = request.user

    if title:
        context["title"] = title

    context["today"] = today

    return context


def verification_connexion(request, utilisateur_autorise):
    if request:
        if not request.user.is_authenticated():
            return redirect("login")
        elif request.user.profile.job.libelle_job not in utilisateur_autorise:
            return redirect(request.user.profile.job.home_job)
        else:
            return None
    else:
        return redirect("login")


def decorateur_verification_connexion(utilisateur_autorise=None):
    if not utilisateur_autorise:
        utilisateur_autorise = []

    def decorateur(view):
        def wrapper_view(request, *args, **kwargs):
            if request:
                if not request.user.is_authenticated():
                    return redirect("login")
                elif request.user.profile.job.libelle_job not in utilisateur_autorise:
                    return redirect(request.user.profile.job.home_job)
                else:
                    return view(request, *args, **kwargs)
            else:
                return redirect("login")
        return wrapper_view
    return decorateur


def ajout_mois(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)


def get_date_fiche_frais():
    today = datetime.date.today()

    if today.day >= 10:
        date_fiche_frais = ajout_mois(today, 1)
    else:
        date_fiche_frais = datetime.date.today()

    return date_fiche_frais


def get_date_fin_fiche_frais():
    today = datetime.date.today()

    if today.day >= 10:
        date_fin_fiche_frais = ajout_mois(datetime.date(today.year, today.month, 10), 1)
    else:
        date_fin_fiche_frais = datetime.date(today.year, today.month, 10)
    
    return date_fin_fiche_frais


def get_temps_relatif(date1, date2):
    return relativedelta(date1, date2).days
