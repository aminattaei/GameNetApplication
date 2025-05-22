from django.contrib import admin
from .models import ContactUs


@admin.register(ContactUs)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "message", "created_time")
    list_filter = ["created_time"]
    ordering = ["-created_time"]
