from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse



class Article(models.Model):
    pic=models.ImageField(_("تصویر"), upload_to="articles/")
    created_time=models.DateField(_("تاریخ قرارگیری در سایت"), auto_now=False, auto_now_add=True)
    write_time=models.DateField(_("زمان نوشتن "), auto_now=False, auto_now_add=False)
    title=models.CharField(_("عنوان"), max_length=50)
    content=models.TextField(_("متن"))
    
    class Meta:
        verbose_name = _("مقاله")
        verbose_name_plural = _("مقالات")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Article_detail", kwargs={"pk": self.pk})
