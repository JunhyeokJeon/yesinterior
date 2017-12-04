from django.conf.urls import url
from user.views import *
from user.forms import LoginForm

from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^login/$', login, { 'template_name': 'register/login.html', 'authentication_form': LoginForm }, name='login'),
    url(r'^logout/$', logout, { 'next_page': '/' }, name='logout'),
    url(r'^register/$', CreateUserView.as_view(), name='register'),
    url(r'^register_done/$', UserCreateDoneTV.as_view(), name='register_done' )
]
