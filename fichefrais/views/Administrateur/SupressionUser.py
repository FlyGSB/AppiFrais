from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from fichefrais.utils import verify_connexion_decorator


@verify_connexion_decorator(utilisateur_autorise=["Administrateur"])
def supression_user(request, user_id=None):

    user = get_object_or_404(User, pk=user_id)

    if user:
        user.delete()

    return redirect("gestion_utilisateur")
