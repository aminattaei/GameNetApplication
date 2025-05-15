from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def ContactUsCreate(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "نظر شما با موفقیت برای تیم ما ارسال گردید.با تشکر از شما"
            )
        else:
            messages.error(
                request,
                "خطایی در ارسال نظر وجود دارد صحت اطلاعات وارد شده را بررسی کنید یا دوباره امتحان کنید.متاسفیم بابت وجود خطا!",
            )

    else:
        form = ContactForm()

    return render(request, "ContactUs/contact.html", context={"form": form})
