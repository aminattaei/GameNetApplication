from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views import generic

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination


from .models import Article, Article_Comment
from .forms import CommentForm
from .serializers import ArticleSerializer


class ArticleListView(generic.ListView):
    model = Article
    context_object_name = "articles"
    template_name = "Articles/blog-sidebar.html"




class ArticleModelViewSet(ReadOnlyModelViewSet):
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    pagination_class = PageNumberPagination
    page_size = 2
    queryset = Article.objects.order_by("-created_time").all()


def Article_Detail(request, pk):
    article = get_object_or_404(Article, id=pk)
    comment_article = Article_Comment.objects.filter(comment_article=article)

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                obj = form.save(commit=False)
                
                
                
                messages.success(request, "نظر شما با موفقیت ثبت شد با تشکراز شما")
            else:
                messages.error(request, "قبل از ارسال نظر وارد شوید")
                return redirect("home_index")
        else:
            form = CommentForm()

    return render(
        request,
        "Articles/blog-details.html",
        context={"article": article, "comments": comment_article, "form": form},
    )
