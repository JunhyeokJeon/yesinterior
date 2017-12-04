from django.views.generic.base import TemplateView
from django.views.generic import ListView
from portfolio.models import Portfolio

class MainPageView(ListView):
    model = Portfolio
    template_name = 'main.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'

class CooperatorPageView(TemplateView):
    template_name = 'cooperator.html'

class VisionPageView(TemplateView):
    template_name = 'vision.html'
