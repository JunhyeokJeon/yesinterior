from django.shortcuts import render
from django.views.generic import ListView, DetailView
from portfolio.models import Portfolio
from django.core.paginator import Paginator
# Create your views here.

class PortfolioLV(ListView):
    model = Portfolio
    paginate_by = 10

    def get_context_date(self, **kwargs):
        context = super(PortfolioListView, self).get_context_date(**kwargs)
        paginator = context=['paginator']
        page_numbers_range = 5
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1)/page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        return context

class PortfolioDV(DetailView):
    model = Portfolio
