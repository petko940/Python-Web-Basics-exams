from django.core.validators import MinLengthValidator
from django.db import models

from June_24_2023_regular_exam.profiles.validators import name_first_letter_validator


# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        validators=(
            MinLengthValidator(2),
            name_first_letter_validator
        )
    )
    last_name = models.CharField(
        max_length=35,
        validators=(
            MinLengthValidator(1),
            name_first_letter_validator
        )
    )
    email = models.EmailField(
        max_length=40,
    )
    password = models.CharField(
        max_length=20,
        validators=(
            MinLengthValidator(8),
        )
    )
    image_url = models.URLField(
        blank=True,
        null=True
    )
    age = models.IntegerField(
        blank=True,
        null=True,
        default=18
    )
