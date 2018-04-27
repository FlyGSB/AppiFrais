from django.shortcuts import redirect


class LoginRequiredMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        url = request.path_info.split("/")
        print(url)
        if not request.user.is_authenticated():
            if not url or not any(url != path for path in ["/login", "/account"]):
                print("redirect login")
                return redirect("login")

        access = True

        if "comptable" in url:
            if not request.user.profile.job.libelle_job in ["comptable", "administrateur"]:
                access = False
        elif "visiteur" in url:
            if not request.user.profile.job.libelle_job in ["visiteur", "administrateur"]:
                access = False
        elif "administrateur" in url:
            if not request.user.profile.job.libelle_job in ["administrateur"]:
                access = False
        if not access:
            return redirect(request.user.profile.job.home_job)

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
