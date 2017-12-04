from django.shortcuts import render
from user.forms import CreateUserForm
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.

class CreateUserView(CreateView):
    template_name = 'register/register.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('user:register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'register/register_done.html'

# LoginRequiredMixin
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)
