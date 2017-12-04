from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^do_order/$', DoOrderView.as_view(), name='do_order'),
    url(r'^do_order_end/$', DoOrderCompleteView.as_view(), name='do_order_end'),
]
