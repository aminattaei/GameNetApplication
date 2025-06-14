from django.contrib.auth import logout, login
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import redirect

from .forms import CustomUserCreationForm

class RegisterUserAccount(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("home_index")
    template_name = "registration/signup.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)