from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User


def supression_user(request, user_id=None):
    """
    :view suppression_user: Permet de supprimer des utilisateurs
    :return: redirige vers la vue de gestion des utilisateurs
    """
    user = get_object_or_404(User, pk=user_id)

    if user:
        user.delete()

    return redirect("gestion_utilisateur")
