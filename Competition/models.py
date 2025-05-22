from django.db import models
from django.utils.translation import gettext as _
from datetime import time
from django.core.exceptions import ValidationError

import os


def validate_file_extensions(value):
        ext=os.path.splitext(value.name)[1]
        valid_extensions=['.mp4', '.mp3', '.avi', '.mov']
        
        if not ext.lower() in valid_extensions:
            raise ValidationError('فرمت فایل معتبر نیست. فقط فایل‌های MP4, MP3, AVI, MOV مجاز هستند.')

class Competition(models.Model):
    title = models.CharField(_("عنوان مسابقه"), max_length=100)
    content = models.TextField(_("توضیحات مسابقه"))
    competition_date = models.DateField(
        _("تاریخ مسابقه"), auto_now=False, auto_now_add=False, default=time()
    )
    video = models.FileField(
        _("ویدیو مسابقه"),
        upload_to="Competitions/videos/%Y/%m/%d",
        null=True,
        blank=True,
        validators=[validate_file_extensions]
    )
    image = models.ImageField(
        _("تصویر مسابقه"), upload_to="Competitions/pictures/%Y/%m/%d"
    )

    class Meta:
        verbose_name = _("مسابقه")
        verbose_name_plural = _("مسابقات")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("Competition_detail", kwargs={"pk": self.pk})
    
    
