from django.shortcuts import render
from django.views import generic
from .models import Competition
from django.template import loader
from django.http import HttpResponse

from rest_framework.permissions import IsAuthenticated

from rest_framework.viewsets import ModelViewSet
from .serializers import CompetitionsSerializer

# class CompetitionsListView(generic.ListView):
#     model = Competition
#     template_name = "Competitions/competitions.html"
#     context_object_name = "Competitions"


class CompetitionsListApiView(ModelViewSet):
    serializer_class = CompetitionsSerializer
    queryset = Competition.objects.all()
    permission_classes=[IsAuthenticated]

def Competitions_List(request):
    Competitions = Competition.objects.all()
    template = loader.get_template("Competitions/competitions.html")
    context = {"Competitions": Competitions}
    return HttpResponse(template.render(context, request))
