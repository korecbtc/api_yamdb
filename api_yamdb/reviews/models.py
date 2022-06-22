from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(
        unique=True,
        max_length=50
    )
    description = models.TextField()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(
        unique=True,
        max_length=50
    )
    description = models.TextField()

    def __str__(self):
        return self.name


class Titles(models.Model):
    name = models.CharField("Произведение", max_length=256)
    # year =

    def __str__(self):
        return self.name


class Review(models.Model):
    pass


class Comment(models.Model):
    pass
