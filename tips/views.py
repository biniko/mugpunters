from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Match, Round



# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"


class TipDetailView(DetailView):
    model = Round
    template_name = "tips.html"

    def get_context_data(self, **kwargs):
        context = super(TipDetailView, self).get_context_data(**kwargs)
        round_id = kwargs['object']
        context['match_list'] = Match.objects.filter(round=round_id)
        return context

