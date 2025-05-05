from django.db import models
from django.utils.translation import gettext as _
from django.utils.timezone import now
from django.urls import reverse
from django.conf import settings

import os
from django.core.exceptions import ValidationError


def validate_file_extensions(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = [".ico", ".svg"]

    if not ext.lower() in valid_extensions:
        return ValidationError(
            "فرمت فایل معتبر نیست. فقط فایل‌های MP4, MP3, AVI, MOV مجاز هستند."
        )


class UpcomingGame(models.Model):
    title = models.CharField(_("عنوان"), max_length=50)
    release_date = models.DateField(_("زمان عرضه"), auto_now=False, auto_now_add=False)
    icon = models.ImageField(
        _("آیکون"), upload_to="Games/icon/", validators=[validate_file_extensions]
    )
    pic = models.ImageField(_("تصویر بازی"), upload_to="Games/pictures/", null=True)

    class Meta:
        verbose_name = _("بازی در حال انتشار")
        verbose_name_plural = _("بازیهای در حال انتشار")

    def __str__(self):
        return self.title

    def get_absolute_url(self):

        return reverse("UpcomingGame_detail", kwargs={"pk": self.pk})


class Game(models.Model):
    title = models.CharField(_("عنوان"), max_length=50)
    launch_date = models.DateField(
        _("زمان راه اندازی"), auto_now=False, auto_now_add=False
    )
    price = models.IntegerField(_("قیمت"), default=0)
    rating = models.IntegerField(_("امتیاز بازی"))
    stars = models.IntegerField(_("تعداد ستاره ها"))
    download_link = models.CharField(
        _("لینک دانلود"),
        max_length=255,
        help_text="اکر لینک در اینجا قرار نگرفت ازابزار های کوتاه کننده ی لینک استفاده کنید",
    )
    pic = models.ImageField(_("تصویر بازی"), upload_to="Games/images", null=True)
    media = models.FileField(_("رسانه"), upload_to="Games/media/", max_length=100)
    description = models.TextField(_("توضیحات"))

    class Meta:
        verbose_name = _("بازی")
        verbose_name_plural = _("بازی ها")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Game_detail", kwargs={"pk": self.pk})


class OperatingSystem(models.Model):
    game = models.ForeignKey(Game, verbose_name=_("بازی ها"), on_delete=models.CASCADE)
    os_name = models.CharField(_("نام سیستم عامل"), max_length=50)
    description = models.TextField(_("توضیحات سیستم عامل"))

    class Meta:
        verbose_name = _("سیستم عامل")
        verbose_name_plural = _("سیستم عامل ها")

    def __str__(self):
        return self.os_name

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("OperatingSystem_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    JOB_LIST = [
        (_("کاربر عادی"), "Normal user"),
        (_("وبلاگ‌نویس"), "Blogger"),
        (_("منتقد بازی"), "Game Critic"),
        (_("توسعه‌دهنده بازی"), "Game Developer"),
        (_("استریمر"), "Streamer"),
        (_("طراح بازی"), "Game Designer"),
        (_("بازیکن حرفه‌ای"), "Pro Gamer"),
    ]

    game = models.ForeignKey("Game", verbose_name=_(" بازی"), on_delete=models.CASCADE)
    user_name = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=_("نام کاربر"), on_delete=models.CASCADE
    )
    job_title = models.CharField(
        _("نقش کاربر"), max_length=50, choices=JOB_LIST, default="کاربر عادی"
    )
    text = models.TextField(_("متن نظر"))
    avatar = models.ImageField(_("آواتار"), upload_to="Games/avatrs/")

    class Meta:
        verbose_name = _("نظر")
        verbose_name_plural = _("نظرات")

    def __str__(self):
        return f"{self.job_title} گفت : {self.text}  "

    def get_absolute_url(self):

        return reverse("Comment_detail", kwargs={"pk": self.pk})


class Tournament(models.Model):
    title = models.CharField(_("عنوان"), max_length=50)
    tournament_date = models.DateField(
        _("زمان مسابقه"), auto_now=False, auto_now_add=False
    )
    image = models.ImageField(_("تصویر مسابقه"), upload_to="Tournaments/%Y/%m/%d")
    video = models.FileField(_("ویدیو مسابقه"), upload_to="Tournaments/videos/")

    class Meta:
        verbose_name = _("مسابقه")
        verbose_name_plural = _("مسابقات")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Tournament_detail", kwargs={"pk": self.pk})


class GameNews(models.Model):
    game = models.ForeignKey(
        "Game", verbose_name=_("اخبار بازی"), on_delete=models.CASCADE
    )

    title = title = models.CharField(_("عنوان خبر بازی"), max_length=50)

    description = models.TextField(_("متن خبر"))

    image = models.ImageField(_("تصویر خبر"), upload_to="GameNews/%Y/%m/%d")

    publish_date = models.DateField(
        _("زمان ایجاد خبر "), auto_now=False, auto_now_add=True
    )

    comment_count = models.CharField(
        _("تعداد نظر"), max_length=50, null=True, blank=True
    )

    class Meta:
        verbose_name = _("خبر بازی")
        verbose_name_plural = _("اخبار بازی")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("GameNews_detail", kwargs={"pk": self.pk})


class TeamMember(models.Model):
    SKILL_TYPES = [
        (_("بازیکن تازه کار"), "Rookie player"),
        (_("بازیکن متوسط "), "Average player"),
        (_("بازیکن حرفه ای"), "Professional player"),
    ]
    name = models.CharField(_("نام  بازیکن"), max_length=50)
    image = models.ImageField(_("تصویر بازیکن"), upload_to="TeamMembers/member_images/")
    skill = models.CharField(
        _("سطح مهارت"), max_length=50, choices=SKILL_TYPES, default="یازیکن تازه کار"
    )

    class Meta:
        verbose_name = _("عضو تیم")
        verbose_name_plural = _("اعضای تیم")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("TeamMember_detail", kwargs={"pk": self.pk})
