from django.shortcuts import render, redirect
from fichefrais.forms import FormPieceJointe
from fichefrais.models import FicheFrais, PiecesJointe
from fichefrais.utils import verify_connexion_decorator, get_date_fiche_frais


@verify_connexion_decorator(utilisateur_autorise=["Visiteur"])
def ajout_piece_jointe(request):

    title = "Ajout Justificatif"

    if request.method == "POST":
        form_piece = FormPieceJointe(request.POST, request.FILES)
        if form_piece.is_valid():
            date_fiche_frais = get_date_fiche_frais()
            fiche_frais = FicheFrais.objects.filter(user=request.user, date__year=date_fiche_frais.year,
                                                    date__month=date_fiche_frais.month).first()
            justificatif = PiecesJointe.objects.filter(fiche_frais=fiche_frais)

            piece_file = form_piece.cleaned_data.get("piece")
            if piece_file:
                if piece_file.name.endswith("php" or "html" or "js"):
                    print("mauvais fichier")
                    return redirect("ajout_justificatif")

            piece = PiecesJointe()
            piece.piece = piece_file
            piece.fiche_frais = fiche_frais
            piece.libelle = piece_file.name
            piece.filename = "%s.%s" % (len(justificatif) + 1, piece_file.name.split(".")[-1])
            piece.save()
            return redirect(request.user.profile.job.home_job)
    else:
        form_piece = FormPieceJointe()

    context = {
        "user": request.user,
        "title": title,
        "form_justificatif": form_piece,
    }

    return render(request, "fichefrais/visiteur/ajout_justificatif.html", context)
