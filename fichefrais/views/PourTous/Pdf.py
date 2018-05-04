from django.views.generic import View
from fichefrais.models import FicheFrais
from fichefrais.utils import liste_fiche_frais, Render


class GeneratePDF(View):

    def get(self, request, id_fiche):
        qs_fiche_frais = FicheFrais.objects.filter(id=id_fiche)
        fiche_frais = liste_fiche_frais(qs_fiche_frais)[qs_fiche_frais[0]]
        return Render.render("fichefrais/fiche_frais_pdf.html", {"fiche_frais": fiche_frais})
