from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm, ProfileRegisterForm


# Create your views here.
def login_view(request):
    title = "Connection"
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
    title = "Inscription"
    form_user = UserRegisterForm(request.POST or None)
    form_profile = ProfileRegisterForm(request.POST or None)

    if form_user.is_valid() and form_profile.is_valid():
        user = form_user.save(commit=False)
        password = form_user.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        form_profile.save(user)
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


def logout_view(request):
    logout(request)
    return redirect("login")
