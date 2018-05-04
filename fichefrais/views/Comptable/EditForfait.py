from django.shortcuts import get_object_or_404, render, redirect

from fichefrais.forms import FormForfait
from fichefrais.models import Forfait


def edit_forfait(request, pk):

    forfait = get_object_or_404(Forfait, pk=pk)
    edit_form = FormForfait(request.POST or None, instance=forfait)

    if edit_form.is_valid():
        edit_form.save()
        return redirect(request.user.profile.job.home_job)

    context = {
        "edit_form": edit_form,
        "element": "Forfait",
        "back": request.user.profile.job.home_job,
    }

    return render(request, "fichefrais/edition_elem_fiche_frais.html", context)
