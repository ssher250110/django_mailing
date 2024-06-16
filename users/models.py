from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Почта", help_text="Введите почту")
    phone = models.CharField(max_length=14, **NULLABLE, verbose_name="Телефон", help_text="Введите номер телефона")
    country = models.CharField(max_length=85, **NULLABLE, verbose_name="Страна", help_text="Введите название страны")
    avatar = models.ImageField(upload_to="users/avatars/", **NULLABLE, verbose_name="Аватар",
                               help_text="Загрузите аватар")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("email",)
