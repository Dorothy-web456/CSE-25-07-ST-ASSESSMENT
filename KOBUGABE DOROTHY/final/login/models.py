from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    confirm_password = models.CharField(max_length=15)

