from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    CHOICES = (('user', 'user'), ('moderator', 'moderator'), ('admin', 'admin'))
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    first_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    role = models.CharField(max_length=150, choices=CHOICES, default='user')
    verification_code = models.IntegerField(blank=True, default='1')
    
    def __str__(self):
        return self.name


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
