from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField("Категория", max_length=256)
    slug = models.SlugField(
        unique=True,
        max_length=50
    )
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Genre(models.Model):
    name = models.CharField("Жанр", max_length=256)
    slug = models.SlugField(
        unique=True,
        max_length=50
    )

    def __str__(self):
        return self.name


class Titles(models.Model):
    name = models.CharField("Произведение", max_length=256)
    # year =

    def __str__(self):
        return self.name
