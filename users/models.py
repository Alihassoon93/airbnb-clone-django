from django.contrib.auth.models import AbstractUser
from django.db import models


# inherits from AbstractUser(default user model)
class User(AbstractUser):

    """Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_CHINESE = "ch"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "En"),
        (LANGUAGE_CHINESE, "Ch"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_RMB = "rmb"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_RMB, "RMB"),
    )

    avatar = models.ImageField(
        blank=True,
        upload_to="avatars",
    )
    gender = models.CharField(
        choices=GENDER_CHOICES,
        max_length=10,
        blank=True,
    )

    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES,
        max_length=2,
        blank=True,
    )

    currency = models.CharField(
        choices=CURRENCY_CHOICES,
        max_length=3,
        blank=True,
    )

    superhost = models.BooleanField(default=False)
