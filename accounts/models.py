from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    avatar = models.ImageField(verbose_name="Аватарка")

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"
