from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    slug = models.SlugField(
        unique=True,
        max_length=50,
        verbose_name='URL'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    slug = models.SlugField(
        unique=True,
        max_length=50,
        verbose_name='URL'
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Titles(models.Model):
    pass


class Review(models.Model):
    pass


class Comment(models.Model):
    pass
