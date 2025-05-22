from django.urls import path

from . import views


urlpatterns = [
    path("", views.ContactUsCreate, name="create_new_contact"),
]
