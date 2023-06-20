from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from .validators import name_validation


# Create your models here.

# plant, plant_type, name, image_url, description, price
# "Outdoor Plants" and "Indoor Plants"
class Plant(models.Model):
    CHOICES = (
        ("Outdoor Plants", "Outdoor Plants"),
        ("Indoor Plants", "Indoor Plants"),
    )

    plant_type = models.CharField(
        max_length=14,
        choices=CHOICES,
    )
    name = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(2),
            name_validation
        ]
    )
    image_url = models.URLField()
    description = models.TextField()
    price = models.FloatField()
