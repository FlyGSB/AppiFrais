from django.conf.urls import url
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^login/', login, {'template_name': 'accounts/new_login.html', "extra_context": {"title": "Identification"}}, name="login"),
    url(r'^logout/$', logout, {'next_page': '/accounts/login/'}, name="logout"),
]
