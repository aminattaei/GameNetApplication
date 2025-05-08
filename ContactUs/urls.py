from django.urls import path

from . import views


urlpatterns = [
    path("", views.ContactCreateView.as_view(), name="create_new_contact"),
]
