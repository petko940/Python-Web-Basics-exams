from django.core.exceptions import ValidationError


def minimum_character(value):
    if len(value) < 2:
        raise ValidationError("The username must be a minimum of 2 chars")
    return value
