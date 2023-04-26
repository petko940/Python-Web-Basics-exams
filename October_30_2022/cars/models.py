from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.db.models import Model


# Create your models here.
def validate_year(value):
    if value < 1980 or value > 2049:
        raise ValidationError('Year must be between 1980 and 2049')


class Car(Model):
    CAR_TYPES = [
        ('Sports Car', 'Sports Car'),
        ('pickup', 'Pickup'),
        ('crossover', 'Crossover'),
        ('minibus', 'Minibus'),
        ('other', 'Other'),
    ]

    type = models.CharField(max_length=10, choices=CAR_TYPES)
    model = models.CharField(max_length=20, validators=[MinLengthValidator(2)])
    year = models.IntegerField(validators=[validate_year])
    image_url = models.URLField(verbose_name="Image URL")
    price = models.FloatField(validators=[MinValueValidator(1)])
