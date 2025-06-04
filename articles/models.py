from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.conf import settings


class Article(models.Model):
    categories=models.ForeignKey("Category", verbose_name=_("دسته"), on_delete=models.CASCADE)
    pic = models.ImageField(_("تصویر"), upload_to="articles/")
    created_time = models.DateField(
        _("تاریخ قرارگیری در سایت"), auto_now=False, auto_now_add=True
    )
    write_time = models.DateField(_("زمان نوشتن "), auto_now=False, auto_now_add=True)
    title = models.CharField(_("عنوان"), max_length=50)
    content = models.TextField(_("متن"))

    class Meta:
        verbose_name = _("مقاله")
        verbose_name_plural = _("مقالات")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Article_detail", kwargs={"pk": self.pk})


class Article_Comment(models.Model):
    article=models.ForeignKey(Article, verbose_name=_("مقاله"), on_delete=models.CASCADE)
    author=models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("نویسنده"), on_delete=models.CASCADE)
    
    email=models.EmailField(_("پست الکترونیکی"), max_length=254)
    message=models.TextField(_('متن نظر'))

    created_time=models.DateField(_("زمان ایجاد نظر"), auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name='نظر'
        verbose_name_plural='نظرات'

    def __str__(self):
        return f' first_name ={self.author} / created_time = {self.created_time} '
    


class Category(models.Model):
    name=models.CharField(_("نام دسته بندی"), max_length=50)
    description=models.TextField(_("توضیحات دسته بندی"),null=True,blank=True)

    class Meta:
        verbose_name = _("دسته بندی")
        verbose_name_plural = _("دسته بندی ها")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})
