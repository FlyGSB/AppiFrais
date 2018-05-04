from django.shortcuts import render, redirect
from datetime import datetime
from fichefrais.forms import FormForfait


def creation_forfait(request):

    today = datetime.today()

    if request.method == "POST":
        form_forfait = FormForfait(request.POST)
        if form_forfait.is_valid():
            form_forfait.save()
            return redirect(request.user.profile.job.home_job)
    else:
        form_forfait = FormForfait()

    context = {
        "user": request.user,
        "today": today,
        "form_forfait": form_forfait,
        "back": request.user.profile.job.home_job,
    }

    return render(request, "fichefrais/comptable/ajout_forfait.html", context)
