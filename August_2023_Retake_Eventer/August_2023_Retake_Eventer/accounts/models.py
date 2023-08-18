from django.core.validators import MinLengthValidator
from django.db import models
from .validators import first_name_only_letter, password_should_have_at_least_one_digit


# Create your models here.
class ProfileModel(models.Model):
    first_name = models.CharField(
        max_length=20,
        validators=[
            first_name_only_letter
        ],
        verbose_name="First Name"
    )
    last_name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(4)
        ],
        verbose_name="Last Name"
    )
    email = models.EmailField(
        max_length=45
    )
    profile_picture = models.URLField(
        blank=True,
        null=True,
        verbose_name="Profile Picture"
    )
    password = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(5),
            password_should_have_at_least_one_digit
        ]
    )
