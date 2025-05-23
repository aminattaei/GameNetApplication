# accounts/views.py

from django.contrib.auth import logout, login
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm

class RegisterUserAccount(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("ShopPage:home-page")
    template_name = "registration/signup.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response



