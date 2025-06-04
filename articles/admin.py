from django.contrib import admin

from .models import Article, Article_Comment,Category


admin.site.register(Article)
admin.site.register(Article_Comment)
admin.site.register(Category)