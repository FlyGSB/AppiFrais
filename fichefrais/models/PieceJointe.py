from django.db import models
from fichefrais.models import FicheFrais
from fichefrais.utils import get_date_fiche_frais


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    date_fiche = get_date_fiche_frais()
    justificatif = PiecesJointe.objects.filter(fiche_frais=instance.fiche_frais)
    extension = filename.split(".")[-1]
    return 'visiteur/user_{0}/{1}/{2}'.format(instance.fiche_frais.user.username,
                                              "%s-%s" % (date_fiche.year, date_fiche.month),
                                              "%s.%s" % (len(justificatif) + 1,  extension))


class PiecesJointe(models.Model):
    fiche_frais = models.ForeignKey(FicheFrais, models.CASCADE, "justificatif")
    libelle = models.CharField(max_length=100)
    date_ajout = models.DateField(auto_now_add=True)
    date_modification = models.DateField(auto_now=True)
    piece = models.FileField(upload_to=user_directory_path, null=True, blank=True)

    def __str__(self):
        return self.libelle
