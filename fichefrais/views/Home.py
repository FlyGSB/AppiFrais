from django.shortcuts import redirect


def home(request):
    user = request.user
    if user.is_authenticated():
        return redirect(user.profile.job.home_job)
    else:
        return redirect("login")
