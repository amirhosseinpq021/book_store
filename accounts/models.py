from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    national_code = models.CharField(max_length=10, null=True, blank=True, unique=True)  # کد ملی
    address = models.TextField(null=True, blank=True)  # آدرس
    postal_code = models.CharField(max_length=10, null=True, blank=True)  # کد پستی

    # استان و شهر
    province = models.CharField(max_length=100, null=True, blank=True)  # استان
    city = models.CharField(max_length=100, null=True, blank=True)  # شهر
