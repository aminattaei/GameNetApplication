from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from zxcvbn_password.fields import PasswordField, PasswordConfirmationField
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "phone_number",'profile_picture', "password1", "password2")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "phone_number",'profile_picture', "is_active", "is_staff")



class RegisterForm(forms.Form):
    password1 = PasswordField()
    password2 = PasswordConfirmationField(confirm_with='password1')