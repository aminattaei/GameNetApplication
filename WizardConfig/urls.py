from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


urlpatterns = [
    # <--- Start Apps Area Urls --- >
    path("admin/", admin.site.urls),
    path("", include("IndexPage.urls")),
    path("games/", include("games.urls")),
    path("competitions/", include("Competition.urls")),
    path("", include("aboutUs.urls"), name="AboutUs_model_config"),
    path("contact-us/", include("ContactUs.urls"), name="Contact-us"),
    path("articles/", include("articles.urls")),
    #< --- Start Apps Area Urls --- >
    
    #< --- Another Settings --- >
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
