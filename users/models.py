from django.contrib.auth.models import AbstractUser
from django.db import models

from mailings.models import NULLABLE


# Create your models here.
class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name="Email")

    avatar = models.ImageField(upload_to="users/avatar/", verbose_name="аватар", **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name="номер телефона", **NULLABLE)
    country = models.CharField(max_length=35, verbose_name="страна", **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
