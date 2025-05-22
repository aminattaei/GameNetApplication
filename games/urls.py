from django.urls import path, include
from . import views

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", views.GamesModelViewSet)

urlpatterns = [
    path("", views.GamesTitlesListView.as_view(), name="games_list"),
    path("<int:pk>/", views.GameDetailView.as_view(), name="game_detail"),
    path("api/", include(router.urls)),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
