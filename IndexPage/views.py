from django.shortcuts import render, get_object_or_404
from django.views import generic
import requests

from games.models import GameNews, Game, Tournament, Comment, UpcomingGame
from Competition.models import Competition
from aboutUs.models import UsTeam


class IndexPageListView(generic.ListView):
    template_name = "IndexPage/index.html"
    model = Game
    context_object_name = "games"

    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["tournaments"] = Tournament.objects.all()
        context["gameNews"] = GameNews.objects.all()
        context["usTeam"] = UsTeam.objects.all()
        context["competitions"] = Competition.objects.all()
        context["upcomingGames"] = UpcomingGame.objects.all()

        return context


class GameNewsDetailView(generic.DetailView):
    model = GameNews
    template_name = "GameNews/GameNews-details.html"
    context_object_name = "gameNews"




class FaqTemplateView(generic.TemplateView):
    template_name='IndexPage/faq.html'


class GalleryListView(generic.ListView):
    model = Game
    context_object_name='pictures'
    template_name = "IndexPage/gallery-3.html"
