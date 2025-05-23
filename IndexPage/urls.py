from django.urls import path
from . import views


urlpatterns = [
    path("", views.IndexPageListView.as_view(), name="home_index"),
    path('<int:pk>/',views.GameNewsDetailView.as_view(),name='GameNews_detail'),
    path("faq/", views.FaqTemplateView.as_view(), name="faq_template"),
    path("gallery/", views.GalleryListView.as_view(), name="gallery_list"),

]