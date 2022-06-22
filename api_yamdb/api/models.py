from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    CHOICES = (('user', 'user'), ('moderator', 'moderator'), ('admin', 'admin'))
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    first_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    role = models.CharField(max_length=150, choices=CHOICES, default='user')