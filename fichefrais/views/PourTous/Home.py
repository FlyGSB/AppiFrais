from django.shortcuts import redirect


def home(request):
    """
    :view home: Vue de redirection vers le bonne Accueil suivant le Job de l'utilisateur
    :return: redirige vers l'acceuil de l'utilisateur
    """
    user = request.user
    if user.is_authenticated():
        return redirect(user.profile.job.home_job)
    else:
        return redirect("login")
