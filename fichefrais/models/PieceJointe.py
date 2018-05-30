from django.db import models
from fichefrais.utils import user_directory_path


class PieceJointe(models.Model):
    """
    :entity PieceJointe: Piece jointe d'une fiche frais (Justificatif)
    :field fiche_frais: fiche frais attache à la piece jointe
    :field libelle: libelle de la piece jointe
    :field date_ajout: date d'ajout dans la base de donnée
    :field date_modification: date de modification de la piece jointe
    :field piece: chemin d'accès à la pièce jointe (recuperer dans la fonction: user_directory_path)
    """
    fiche_frais = models.ForeignKey("FicheFrais", models.CASCADE, "justificatif")
    libelle = models.CharField(max_length=100)
    date_ajout = models.DateField(auto_now_add=True)
    date_modification = models.DateField(auto_now=True)
    piece = models.FileField(upload_to=user_directory_path, null=True, blank=True)

    def __str__(self):
        return self.libelle
