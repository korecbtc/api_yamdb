from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


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


class Title(models.Model):
    pass


class Review(models.Model):
    text = models.TextField(verbose_name='Текст отзыва')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата публикации')
    score = models.IntegerField(validators=(MinValueValidator(1),
                                            MaxValueValidator(10)),
                                verbose_name='Рейтинг')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='reviews',
                               verbose_name='Автор')
    title = models.ForeignKey(Title,
                              on_delete=models.CASCADE,
                              related_name='reviews',
                              verbose_name='Произведение')

    class Meta:
        ordering = ['-pub_date']
        constraints = [
            models.UniqueConstraint(fields=('title', 'author'),
                                    name='Unique_review_per_author')
        ]
        verbose_name = 'Обзор'
        verbose_name_plural = 'Обзоры'


class Comment(models.Model):
    review = models.ForeignKey(Review,
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True,
                               related_name='comments',
                               verbose_name='Обзор'
                               )
    text = models.TextField(verbose_name='Текст комментария')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='comments',
                               verbose_name='Автор',
                               )
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата публикации комментария')

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
