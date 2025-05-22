from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("competitions", views.CompetitionsListApiView)

urlpatterns = [
    # path("", views.CompetitionsListView.as_view(), name="matchs_list"),
    path("", views.Competitions_List, name="matchs_list"),
    path("api/", include(router.urls)),
]
