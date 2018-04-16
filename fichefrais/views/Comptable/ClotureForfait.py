from datetime import datetime
from fichefrais.models import Forfait
from fichefrais.utils import verify_connexion_decorator
from django.shortcuts import redirect, get_object_or_404


@verify_connexion_decorator(utilisateur_autorise=["Comptable"])
def cloture_forfait(request, pk=None):

    today = datetime.today()
    forfait = get_object_or_404(Forfait, pk=pk)
    forfait.date_fin = today
    forfait.save()

    return redirect(request.user.profile.job.home_job)