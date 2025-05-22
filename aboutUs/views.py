from django.shortcuts import render
from django.views import generic

from .models import UsTeam
from Competition.models import Competition


class TeamListView(generic.ListView):
    model = UsTeam
    context_object_name = "users"
    template_name = "AboutUs/team.html"


class AboutUsListView(generic.ListView):
    model = UsTeam
    context_object_name = "users"
    template_name = "AboutUs/about.html"

    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["competitions"] = Competition.objects.all()
        return context
