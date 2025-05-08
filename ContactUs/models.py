from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactUs(models.Model):
    name = models.CharField(_("نام"), max_length=50)
    email = models.EmailField(_("ایمیل"), max_length=254)
    subject = models.CharField(_("موضوع"), max_length=50)
    message = models.TextField(_("پیام "))
    created_time = models.DateTimeField(
        _("زمان ایجاد پیغام"), auto_now=False, auto_now_add=True
    )

    class Meta:
        verbose_name = _("ContactUs")
        verbose_name_plural = _("ContactUss")

    def __str__(self):
        return f"Name: {self.name} / Time: {self.created_time}"

    # def get_absolute_url(self):
    #     from django.urls import reverse

    #     return reverse("ContactUs_detail", kwargs={"pk": self.pk})
