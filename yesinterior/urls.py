"""yesinterior URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

from yesinterior.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', MainPageView.as_view(), name='main'),

    url(r'^portfolio/', include('portfolio.urls', namespace='portfolio')),
    url(r'^accounts/', include('user.urls', namespace='user')),
    url(r'^order/', include('order.urls', namespace='order')),
    url(r'^contact/$', ContactPageView.as_view(), name='contact'),
    url(r'^vision/$', VisionPageView.as_view(), name='vision'),
    url(r'^cooperator/$', CooperatorPageView.as_view(), name='cooperator'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
