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
    comments = Article_Comment.objects.filter(article=article)
    form = CommentForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            if request.user.is_authenticated:
                comment = form.save(commit=False)
                comment.article = article
                comment.author = request.user
                comment.email = request.user.email or 'no@email.com'
                comment.save()
                messages.success(request, "نظر شما با موفقیت ثبت شد. با تشکر از شما.")
                return redirect(request.path)
            else:
                messages.error(request, "قبل از ارسال نظر وارد شوید")
                return redirect("home_index")
        else:
            messages.error(request,'نام کاربری یا رمز عبور صحیح نمی باشد!')

    return render(request, "Articles/blog-details.html", {
        "article": article,
        "comments": comments,
        "form": form,
    })
