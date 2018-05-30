from django.views.generic import View
from fichefrais.models import FicheFrais
from fichefrais.utils import liste_fiche_frais, Render


class GeneratePDF(View):
    """
    :view GeneratePdf: permet de generer un pdf
    :template fiche_frais_pdf.html:
    """
    def get(self, request, id_fiche):
        """
        Permet de recuperer le fichier PDF
        :param id_fiche: clef primaire d'une Fiche de Frais
        :return: rendu du PDF
        """
        qs_fiche_frais = FicheFrais.objects.filter(id=id_fiche)
        fiche_frais = liste_fiche_frais(qs_fiche_frais)[qs_fiche_frais[0]]
        return Render.render("fichefrais/fiche_frais_pdf.html", {"fiche_frais": fiche_frais})
