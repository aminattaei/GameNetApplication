from django.shortcuts import render
from django.views import generic

from .models import ContactUs


class ContactCreateView(generic.CreateView):
    model = ContactUs
    fields = ("name", "email", "subject", "message")
    template_name = "ContactUs/contact.html"
