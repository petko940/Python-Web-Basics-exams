from django.core.exceptions import ValidationError


def year_validator(value):
    if value < 1980 or value > 2049:
        raise ValidationError("Year must be between 1980 and 2049")
