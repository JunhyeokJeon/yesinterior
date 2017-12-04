from django.shortcuts import render
from order.forms import DoOrderForm
from order.models import Order

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from user.views import LoginRequiredMixin

# Create your views here.

class DoOrderView(LoginRequiredMixin, CreateView):
    form_class = DoOrderForm
    template_name = 'order/do_order.html'
    success_url = reverse_lazy('order:do_order_end')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(DoOrderView, self).form_valid(form)

class DoOrderCompleteView(TemplateView):
    template_name = 'order/do_order_end.html'
