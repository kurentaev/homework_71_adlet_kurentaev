from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from accounts.managers import UserManager
from django.db.models import TextChoices


class GenderChoices(TextChoices):
    OTHER = 'other', 'Other'
    MALE = 'male', 'Male'
    FEMALE = 'female', 'Female'


class Account(AbstractUser):
    username = models.CharField(
        verbose_name='Username',
        max_length=100,
        null=False,
        blank=False,
        unique=True,
    )
    email = models.EmailField(
        verbose_name='Email',
        unique=True,
        null=False,
        blank=False,
    )
    avatar = models.ImageField(
        null=False,
        blank=False,
        upload_to='avatars',
        verbose_name='Avatar'
    )
    about_user = models.TextField(
        verbose_name="About user",
        null=True,
        blank=True,
    )
    phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    gender = models.CharField(
        verbose_name='Gender',
        choices=GenderChoices.choices,
        max_length=100,
        default=GenderChoices.OTHER
    )
    liked_posts = models.ManyToManyField(
        verbose_name='Liked posts',
        to='posts.Post',
        related_name='user_likes'
    )
    subscriptions = models.ManyToManyField(
        verbose_name='Subscriptions',
        to='accounts.Account',
        related_name='subscribers'
    )
    commented_posts = models.ManyToManyField(
        verbose_name='Commented posts',
        to='posts.Post',
        related_name='user_comments'
    )
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'email',
        'avatar',
        'password'
    ]

    objects = UserManager()

    def __str__(self):
        return f"{self.email} - {self.gender}"

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
