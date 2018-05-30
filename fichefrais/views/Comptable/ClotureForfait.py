from datetime import datetime
from fichefrais.models import Forfait
from django.shortcuts import redirect, get_object_or_404


def cloture_forfait(request, pk=None):
    """
    :view cloture_forfait: Permet de cloturer un forfait
    :param pk: clef primaire d'un Forfait
    :return: redirige vers l'accueil de l'utilisateur
    """
    today = datetime.today()
    forfait = get_object_or_404(Forfait, pk=pk)
    forfait.date_fin = today
    forfait.save()

    return redirect(request.user.profile.job.home_job)
