import datetime

from django.core.exceptions import ValidationError


def prevent_date_earlier_than_today(value):
    if value < datetime.date.today():
        raise ValidationError("The date cannot be in the past!")
