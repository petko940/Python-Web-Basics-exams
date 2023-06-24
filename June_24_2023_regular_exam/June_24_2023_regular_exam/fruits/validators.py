from django.core.exceptions import ValidationError


def fruit_name_validator(value):
    if not value.isalpha():
        raise ValidationError("Fruit name should contain only letters!")