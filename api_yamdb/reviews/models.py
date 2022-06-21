from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(
        unique=True,
        max_length=50
    )
    description = models.TextField()

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


class Title(models.Model):
    pass


class Comment(models.Model):
    pass


class Review(models.Model):
    pass
