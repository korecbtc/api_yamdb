from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from api.models import User


class Title(models.Model):
    pass


class Review(models.Model):
    text = models.TextField(verbose_name='Текст отзыва')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата публикации')
    rating = models.IntegerField(validators=(MinValueValidator(1),
                                             MaxValueValidator(10)),
                                 verbose_name='Рейтинг')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='reviews',
                               verbose_name='Автор')
    titles = models.ForeignKey(Title,
                               on_delete=models.CASCADE,
                               related_name='reviews',
                               verbose_name='Произведение')

    class Meta:
        ordering = ['-pub_date']
        constraints = models.UniqueConstraint(fields=('title', 'author'),
                                              name='Unique_review_per_author')
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
