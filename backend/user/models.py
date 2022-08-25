from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """User`s model"""

    first_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64, blank=True)
    email = models.EmailField(unique=True)

    class Meta(AbstractUser.Meta):
        verbose_name = 'Модель пользователя'
        verbose_name_plural = 'Модели пользователей'
        ordering = ['-date_joined']
