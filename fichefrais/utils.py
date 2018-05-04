import datetime
import calendar
from dateutil.relativedelta import relativedelta
from django.shortcuts import get_object_or_404, redirect
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


class Render:

    @staticmethod
    def render(path: str, params: dict):
        template = get_template(path)
        html = template.render(params)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            return HttpResponse(response.getvalue(), content_type='application/pdf')
        else:
            return HttpResponse("Erreur Rendu PDF", status=400)


def liste_fiche_frais(qs_fiche_frais):
    from fichefrais.models import LigneFraisForfait, LigneFraisHorsForfait, PieceJointe
    fiches_frais = {}
    for fiche in qs_fiche_frais:
        frais_forfait = LigneFraisForfait.objects.filter(fiche_frais=fiche)
        frais_hors_forfait = LigneFraisHorsForfait.objects.filter(fiche_frais=fiche)
        justificatif = PieceJointe.objects.filter(fiche_frais=fiche)
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
            "total": fiche.montant_valide,
        }
    return fiches_frais


def get_elem_fiche(type_elem=None, obj_id=None):
    from fichefrais.models import LigneFraisForfait, LigneFraisHorsForfait, PieceJointe, Forfait
    elem = None

    if obj_id and type_elem:
        if type_elem == "frais_forfait":
            elem = get_object_or_404(LigneFraisForfait, pk=obj_id)
        elif type_elem == "frais_hors_forfait":
            elem = get_object_or_404(LigneFraisHorsForfait, pk=obj_id)
        elif type_elem == "justificatif":
            elem = get_object_or_404(PieceJointe, pk=obj_id)
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


def verification_connexion(request, utilisateur_autorise: list):
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


def user_directory_path(instance, filename):
    from fichefrais.models import PieceJointe
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    date_fiche = get_date_fiche_frais()
    justificatif = PieceJointe.objects.filter(fiche_frais=instance.fiche_frais)
    extension = filename.split(".")[-1]
    return 'visiteur/user_{0}/{1}/{2}'.format(instance.fiche_frais.user.username,
                                              "%s-%s" % (date_fiche.year, date_fiche.month),
                                              "%s.%s" % (len(justificatif) + 1,  extension))


def set_montant_valide(fiche_frais):
    from fichefrais.models import LigneFraisForfait, LigneFraisHorsForfait, FicheFrais
    if isinstance(fiche_frais, FicheFrais):
        f = LigneFraisForfait.objects.filter(fiche_frais=fiche_frais, etat__valeur=3)
        hf = LigneFraisHorsForfait.objects.filter(fiche_frais=fiche_frais, etat__valeur=3)
        total = round(sum([t.total for t in f]) + sum([t.total for t in hf]), 2)
        fiche_frais.montant_valide = total
        fiche_frais.save()
