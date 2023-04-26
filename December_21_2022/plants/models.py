from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Model
from django.core import validators


# Create your models here.
def name_validator(value: str):
    if not value.isalpha():
        raise ValidationError("Plant name should contain only letters!")


class Plant(Model):
    types = [
        ('Outdoor Plants', 'Outdoor Plants'),
        ('Indoor Plants', 'Indoor Plants')
    ]

    plant_type = models.CharField(max_length=14, choices=types)
    name = models.CharField(max_length=20, validators=[validators.MinLengthValidator(2), name_validator])
    image_url = models.URLField(verbose_name="Image URL")
    description = models.TextField()
    price = models.FloatField()
