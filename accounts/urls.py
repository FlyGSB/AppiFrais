from django.conf.urls import url

# from .views import login_view, logout_view, register_view
from django.contrib.auth.views import login, logout
# from .forms import UserLoginForm


urlpatterns = [
    # url(r'^login/$', login_view, name='login'),
    # url(r'^logout/$', logout_view, name='logout'),
    # url(r'^register/$', register_view, name='register')
    url(r'^login/', login, {'template_name': 'accounts/new_login.html',}, name="login"),
    url(r'^logout/$', logout, {'next_page': '/login'}, name="logout"),
]
