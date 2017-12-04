from django.conf.urls import url
from portfolio.views import *

urlpatterns = [
    url(r'^$', PortfolioLV.as_view(), name='portfolio'),
    url(r'^(?P<pk>\d+)/$', PortfolioDV.as_view(), name='portfolio_detail'),
]
