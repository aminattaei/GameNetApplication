from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", views.ArticleModelViewSet)

urlpatterns = [
    path("", views.ArticleListView.as_view(), name="articles_list"),
    path("<int:pk>/", views.Article_Detail, name="Article_detail"),
    path("api/", include(router.urls)),
]
