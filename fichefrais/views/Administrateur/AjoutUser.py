from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.conf import settings
from accounts.forms import UserLoginForm, UserRegisterForm, ProfileRegisterForm

def ajout_user(request):
    title = "Ajout Utilisateur"
    form_user = UserRegisterForm(request.POST or None)
    form_profile = ProfileRegisterForm(request.POST or None)

    if form_user.is_valid() and form_profile.is_valid():
        user = form_user.save(commit=False)
        password = form_user.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        form_profile.save(user)
        return redirect("home_admin")

    context = {
        "user": request.user,
        "form_user": form_user,
        "form_profile": form_profile,
        "title": title,
        "back": request.user.profile.job.home_job,
    }
    return render(request, "fichefrais/administrateur/ajout_user.html", context)
