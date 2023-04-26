import profile

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.

def validate_username(value):
    if len(value) < 2:
        raise ValidationError("The username must be a minimum of 2 chars")


class Profile(models.Model):
    username = models.CharField(max_length=10, validators=[validate_username])
    email = models.EmailField()
    age = models.IntegerField(validators=[MinValueValidator(18)])
    password = models.CharField(max_length=30)
    first_name = models.CharField(blank=True, null=True, max_length=30, verbose_name='First Name')
    last_name = models.CharField(blank=True, null=True, max_length=30, verbose_name='Last Name')
    profile_picture = models.URLField(blank=True, null=True)
