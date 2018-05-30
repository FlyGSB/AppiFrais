from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm, ProfileRegisterForm


def login_view(request):
    """
    Vue de connexion des utilisateurs
    :return: redirige vers le menu de l'utilisateur connecte
    """
    title = "Connexion"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect(user.profile.job.home_job)

    context = {
        "form": form,
        "title": title,
        "user": request.user,
    }

    return render(request, "accounts/login.html", context)


def register_view(request):
    """
    Vue de creation d'un utilisateur
    :return: redirige vers la page de connexion
    """
    title = "Inscription"
    form_user = UserRegisterForm(request.POST or None)
    form_profile = ProfileRegisterForm(request.POST or None)

    if form_user.is_valid() and form_profile.is_valid():
        user = form_user.save(commit=False)
        password = form_user.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        form_profile.save(user=user)
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect("login")

    context = {
        "user": request.user,
        "form_user": form_user,
        "form_profile": form_profile,
        "title": title,
    }
    return render(request, "accounts/register.html", context)


def register_view2(request):
    """
    Vue de creation d'un utilisateur par un administrateur
    :return: redirige vers le menu de l'administrateur
    """
    title = "Ajout Utilisateur"
    form_user = UserRegisterForm(request.POST or None)
    form_profile = ProfileRegisterForm(request.POST or None)

    if form_user.is_valid() and form_profile.is_valid():
        user = form_user.save(commit=False)
        password = form_user.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        form_profile.save(user=user)
        return redirect("home_admin")

    context = {
        "user": request.user,
        "form_user": form_user,
        "form_profile": form_profile,
        "title": title,
        "back": request.user.profile.job.home_job,
    }
    return render(request, "fichefrais/administrateur/ajout_user.html", context)


def logout_view(request):
    """
    Vue de deconnexion
    :return: redirige vers la vue de connexion
    """
    logout(request)
    return redirect("login")
