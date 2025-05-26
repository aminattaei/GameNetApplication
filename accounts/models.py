from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to="profile/images/")
    
