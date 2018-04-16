from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login")
def home(request):
    user = request.user
    if user.is_authenticated():
        return redirect(user.profile.job.home_job)
    else:
        return redirect("login")
