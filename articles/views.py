from django.shortcuts import render
from django.views import generic

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination
from .serializers import ArticleSerializer

from .models import Article


class ArticleListView(generic.ListView):
    model = Article
    context_object_name = "articles"
    template_name = "Articles/blog-sidebar.html"


class ArticleDetailView(generic.DetailView):
    model = Article
    context_object_name = "article"
    template_name = "Articles/blog-details.html"


class ArticleModelViewSet(ReadOnlyModelViewSet):
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    pagination_class = PageNumberPagination
    page_size = 2
    queryset = Article.objects.order_by("-created_time").all()
