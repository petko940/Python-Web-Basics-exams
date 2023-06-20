from django.core.validators import MinLengthValidator
from django.db import models
from .validators import start_letter

# Create your models here.
# profile, username, first_name, last_name, profile_picture,


class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        validators=[
            MinLengthValidator(2),
        ]
    )
    first_name = models.CharField(
        max_length=20,
        validators=[
            start_letter
        ]
    )
    last_name = models.CharField(
        max_length=20,
        validators=[
            start_letter
        ]
    )
    profile_picture = models.URLField(
        blank=True,
        null=True
    )
