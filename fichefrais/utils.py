import datetime
import calendar
from dateutil.relativedelta import relativedelta
from django.shortcuts import get_object_or_404
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

"""
Fichier remplis d'utilitaire pour l'application
"""

class Render:
    """
    Class Render pour les rendus de fichier PDF
    """
    @staticmethod
    def render(path: str, params: dict):
        """
        Permet de recuper un template et de le transformer en PDF en lui injectant un Context
        :param path: chemin du template
        :param params: dictionnaire de parametre
        :return: reponse Http de type application/pdf
        """
        template = get_template(path)
        html = template.render(params)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            return HttpResponse(response.getvalue(), content_type='application/pdf')
        else:
            return HttpResponse("Erreur Rendu PDF", status=400)


def liste_fiche_frais(qs_fiche_frais):
    """
    Fonction de formatage des requetes pour un Fiche de Frais
    :param qs_fiche_frais: requete d'une ou plusieurs Fiche de Frais
    :return: une liste de Fiche de Frais pretes a etre utilise dans une vue
    """
    from fichefrais.models import LigneFraisForfait, LigneFraisHorsForfait, PieceJointe
    fiches_frais = {}
    for fiche in qs_fiche_frais:
        frais_forfait = LigneFraisForfait.objects.filter(fiche_frais=fiche)
        frais_hors_forfait = LigneFraisHorsForfait.objects.filter(fiche_frais=fiche)
        justificatif = PieceJointe.objects.filter(fiche_frais=fiche)
        sous_total_frais_forfait = round(sum([ligne.total for ligne in frais_forfait]), 2)
        sous_total_frais_hors_forfait = round(sum([ligne.montant for ligne in frais_hors_forfait]), 2)
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
    """
    Permet de recuperer un element d'une Fiche de Frais rapidement
    :param type_elem: le type de l'element (ligne_frais_forfait, ligne_frais_hors_forfait, forfait, piece_jointe)
    :param obj_id: clef primaire de l'element
    :return: la requete de l'element
    """
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


def ajout_mois(sourcedate, months):
    """
    Permet d'ajouter un mois a une date
    :param sourcedate: la date source
    :param months: nombre de mois en plus ou moins
    :return: la date transforme
    """
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)


def get_date_fiche_frais():
    """
    Permet de recuperer facilement la date des Fiche de Frais a traiter
    :return: si le jour > 10: la date +1 mois sinon la date d'aujourd'hui
    """
    today = datetime.date.today()

    if today.day >= 10:
        date_fiche_frais = ajout_mois(today, 1)
    else:
        date_fiche_frais = datetime.date.today()

    return date_fiche_frais


def get_date_fin_fiche_frais():
    """
    Permet de recuperer facilement la date d'echeance d'une Fiche de Frais
    :return: date de fin des Fiche de Frais
    """
    today = datetime.date.today()

    if today.day >= 10:
        date_fin_fiche_frais = ajout_mois(datetime.date(today.year, today.month, 10), 1)
    else:
        date_fin_fiche_frais = datetime.date(today.year, today.month, 10)
    
    return date_fin_fiche_frais


def get_temps_relatif(date1, date2):
    """
    Recupere le temps relatif entre 2 date
    :param date1: premiere date
    :param date2: deuxieme date
    :return: nombre de jour qui separe les deux date
    """
    return relativedelta(date1, date2).days


def user_directory_path(instance, filename):
    """
    Permet de generer le chemin de stockage des Piece Jointe
    :param instance: instance d'une Fiche de Frais
    :param filename: nom du fichier
    :return: chemin d'acces/sauvegarde d'une PieceJointe
    """
    from fichefrais.models import PieceJointe
    # les fichier seront upload dans MEDIA_ROOT/user_<id>/<filename>
    date_fiche = get_date_fiche_frais()
    justificatif = PieceJointe.objects.filter(fiche_frais=instance.fiche_frais)
    extension = filename.split(".")[-1]
    return 'visiteur/user_{0}/{1}/{2}'.format(instance.fiche_frais.user.username,
                                              "%s-%s" % (date_fiche.year, date_fiche.month),
                                              "%s.%s" % (len(justificatif) + 1,  extension))


def set_montant_valide(fiche_frais):
    """
    Permet de calculer le montant valide d'une Fiche de Frais
    :param fiche_frais: requete de la fiche de frais a valider le montant
    """
    from fichefrais.models import LigneFraisForfait, LigneFraisHorsForfait, FicheFrais
    if isinstance(fiche_frais, FicheFrais):
        f = LigneFraisForfait.objects.filter(fiche_frais=fiche_frais, etat__valeur=3)
        hf = LigneFraisHorsForfait.objects.filter(fiche_frais=fiche_frais, etat__valeur=3)
        total = round(sum([t.total for t in f]) + sum([t.total for t in hf]), 2)
        fiche_frais.montant_valide = total
        fiche_frais.save()
