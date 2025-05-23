from django.urls import path
from .views import RegisterUserAccount


urlpatterns = [
    path("register/", RegisterUserAccount.as_view(), name="register"),
]
