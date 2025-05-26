from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class UsTeam(models.Model):
    pic = models.ImageField(_("تصویر شخص"), upload_to="AboutUs/team/image/")
    name = models.CharField(_("نام شخص"), max_length=50)
    job = models.CharField(_("مهارت کاربر"), max_length=50)
    twitter_user_link = models.CharField(
        _("لینک توییتر کاربر"), max_length=50, null=True, blank=True
    )
    facebook_user_link = models.CharField(
        _("لینک فیسبوک کاربر"), max_length=50, null=True, blank=True
    )
    instagram_user_link = models.CharField(
        _("لینک اینستاگرام کاربر"), max_length=50, null=True, blank=True
    )

    class Meta:
        verbose_name = _("تیم")
        verbose_name_plural = _("تیم ها")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("MyTeam_detail", kwargs={"pk": self.pk})
