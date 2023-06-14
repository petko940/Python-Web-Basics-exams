from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


# Create your models here.
def validate_username(value):
    if not all(c.isalnum() or c == '_' for c in value):
        print(type(value))
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


class Profile(models.Model):
    username = models.CharField(
        max_length=15, validators=[validate_username, MinLengthValidator(2)]
    )
    email = models.EmailField()
    age = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0)])
