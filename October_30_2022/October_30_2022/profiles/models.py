from django.core.validators import MinValueValidator
from django.db import models
from .validators import minimum_character


# Create your models here.
class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        validators=[minimum_character])

    email = models.EmailField()
    age = models.IntegerField(validators=[MinValueValidator(18)])
    password = models.CharField(max_length=30)
    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=30,
        verbose_name="First Name")

    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=30,
        verbose_name="Last Name")

    profile_picture = models.URLField()
