from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactUs(models.Model):
    name = models.CharField(_("نام"), max_length=50)
    email = models.EmailField(_("ایمیل"), max_length=254)
    subject = models.CharField(_("موضوع"), max_length=50)
    message = models.TextField(_("پیام "))

    class Meta:
        verbose_name = _("ContactUs")
        verbose_name_plural = _("ContactUss")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     from django.urls import reverse

    #     return reverse("ContactUs_detail", kwargs={"pk": self.pk})
