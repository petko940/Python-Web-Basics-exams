from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from October_30_2022.cars.validators import year_validator


# Create your models here.
class Car(models.Model):
    CHOICES = (
        ("Sports Car", "Sports Car"),
        ("Pickup", "Pickup"),
        ("Crossover", "Crossover"),
        ("Minibus", "Minibus"),
        ("Other", "Other")
    )

    type = models.CharField(
        choices=CHOICES,
        max_length=10)
    model = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(2)])

    year = models.IntegerField(validators=[year_validator])
    image_url = models.URLField()
    price = models.FloatField(validators=[MinValueValidator(1)])
