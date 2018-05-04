from django.shortcuts import render, redirect
from fichefrais.forms import FormPieceJointe
from fichefrais.models import FicheFrais, PieceJointe
from fichefrais.utils import get_date_fiche_frais


def ajout_piece_jointe(request):

    title = "Ajout Justificatif"

    if request.method == "POST":
        form_piece = FormPieceJointe(request.POST, request.FILES)
        if form_piece.is_valid():
            date_fiche_frais = get_date_fiche_frais()
            fiche_frais = FicheFrais.objects.get(user=request.user, date__year=date_fiche_frais.year,
                                                    date__month=date_fiche_frais.month)
            justificatif = PieceJointe.objects.filter(fiche_frais=fiche_frais)

            piece_file = form_piece.cleaned_data.get("piece")
            if piece_file:
                if piece_file.name.endswith("php" or "html" or "js" or "py"):
                    print("mauvais fichier")
                    return redirect("ajout_justificatif")

            piece = PieceJointe()
            piece.piece = piece_file
            piece.fiche_frais = fiche_frais
            piece.libelle = piece_file.name
            piece.filename = "%s.%s" % (justificatif.count() + 1, piece_file.name.split(".")[-1])
            piece.save()
            fiche_frais.nb_justificatif += 1
            fiche_frais.save()
            return redirect(request.user.profile.job.home_job)
    else:
        form_piece = FormPieceJointe()

    context = {
        "user": request.user,
        "title": title,
        "form_justificatif": form_piece,
    }

    return render(request, "fichefrais/visiteur/ajout_justificatif.html", context)
