from django.core.validators import MinLengthValidator
from django.db import models

from June_24_2023_regular_exam.fruits.validators import fruit_name_validator


# Create your models here.
class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        validators=(
            MinLengthValidator(2),
            fruit_name_validator
        ),
    )
    image_url = models.URLField()
    description = models.TextField()
    nutrition = models.TextField(
        blank=True,
        null=True,
    )
