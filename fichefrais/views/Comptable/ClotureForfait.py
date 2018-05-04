from datetime import datetime
from fichefrais.models import Forfait
from django.shortcuts import redirect, get_object_or_404


def cloture_forfait(request, pk=None):

    today = datetime.today()
    forfait = get_object_or_404(Forfait, pk=pk)
    forfait.date_fin = today
    forfait.save()

    return redirect(request.user.profile.job.home_job)
