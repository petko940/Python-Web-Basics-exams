import profile

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import Model


# Create your models here.
def name_validator(value):
    if not value[0].isupper():
        raise ValidationError("Your name must start with a capital letter!")


class Profile(Model):
    username = models.CharField(max_length=10, validators=[MinLengthValidator(2)])
    first_name = models.CharField(verbose_name='First Name', max_length=20, validators=[name_validator])
    last_name = models.CharField(verbose_name='Last Name', max_length=20, validators=[name_validator])
    profile_picture = models.URLField(blank=True, null=True)
