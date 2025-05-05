from django.shortcuts import render
from django.views import generic

from .models import Game
from Competition.models import Competition

from .serializers import GameModelSerializer

from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class GamesTitlesListView(generic.ListView):
    model = Game
    template_name = "Games/games.html"
    context_object_name = "Games"


class GameDetailView(generic.DetailView):
    model = Game
    template_name = "Games/single-game.html"
    context_object_name = "Game"


class GamesModelViewSet(ModelViewSet):
    serializer_class = GameModelSerializer
    queryset = Game.objects.all()

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


