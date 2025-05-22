from django.urls import path
from . import views

urlpatterns = [
    path("team/", views.TeamListView.as_view(), name="team_members_list"),
    path("about-us/", views.AboutUsListView.as_view(), name="about-us"),
]
