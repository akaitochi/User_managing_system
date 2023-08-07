from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Class for users."""

    ROLES_CHOICES = [
        ('user', 'User'),
        ('moderator', 'Moderator'),
        ('admin', 'Admin')
    ]
    username = models.CharField(
        verbose_name='Username',
        max_length=150,
        unique=True,
    )
    first_name = models.CharField(
        verbose_name='Name',
        max_length=150,
        blank=True
    )
    last_name = models.CharField(
        verbose_name='Surname',
        max_length=150,
        blank=True
    )
    email = models.EmailField(
        verbose_name='Email',
        max_length=254,
        unique=True,
    )
    bio = models.TextField(verbose_name='Bio', blank=True,)

    @property
    def is_moderator(self):
        return self.role == 'moderator'

    @property
    def is_admin(self):
        return self.role == 'admin'

    class Meta:
        ordering = ['username']
