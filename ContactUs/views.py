from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import get_user_model
from .forms import ContactForm

User = get_user_model()

from .models import ContactUs


# class ContactCreateView(generic.CreateView):
#     model = ContactUs
#     fields = ("name", "email", "subject", "message")
#     template_name = "ContactUs/contact.html"

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         queryset.user = self.user


def ContactUsCreate(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            if request.user.is_authenticated:
                obj.name = request.user.username
                obj.email = request.user.email
            obj.save()
            return redirect("ContactUs/contact-done.html")
    else:
        form = ContactForm()

    return render(request, "ContactUs/contact.html", context={"form": form})
