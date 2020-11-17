from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    avatar = models.ImageField(verbose_name="Аватарка", blank=True)

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
