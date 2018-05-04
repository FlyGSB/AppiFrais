from django.db import models
from fichefrais.utils import user_directory_path


class PieceJointe(models.Model):
    fiche_frais = models.ForeignKey("FicheFrais", models.CASCADE, "justificatif")
    libelle = models.CharField(max_length=100)
    date_ajout = models.DateField(auto_now_add=True)
    date_modification = models.DateField(auto_now=True)
    piece = models.FileField(upload_to=user_directory_path, null=True, blank=True)

    def __str__(self):
        return self.libelle
