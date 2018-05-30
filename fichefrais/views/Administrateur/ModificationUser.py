from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from accounts.forms import UserRegisterForm


def modification_user(request, user_id=None):
    """
    :view modification_user: Permet la modification des utilisateurs par formulaire
    :template register.html:
    """
    if not user_id:
        if "user_modif" in request.session:
            if request.session["user_modif"]:
                user = get_object_or_404(User, request.session["user_modif"])
                del request.session["user_modif"]
            else:
                return redirect(request.user.profile.job.home_job)
        else:
            return redirect(request.user.profile.job.home_job)
    else:
        user = get_object_or_404(User, pk=user_id)
        if user:
            request.session["user_modif"] = user_id

    form = UserRegisterForm(request.POST or None, instance=user)

    if form.is_valid():
        password = form.cleaned_data.get("password")
        username = form.cleaned_data.get("username")
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        email = form.cleaned_data.get("email")

        if username:
            user.username = username
        if last_name:
            user.last_name = last_name
        if first_name:
            user.first_name = first_name
        if email:
            user.email = email
        if password:
            user.profile.changer_mdp = True
            user.set_password(password)
            user.profile.save()

        user.save()
        return redirect(request.user.profile.job.home_job)

    context = {
        "user": request.user,
        "form_user": form,
        "title": "Modification",
    }

    return render(request, "accounts/register.html", context)