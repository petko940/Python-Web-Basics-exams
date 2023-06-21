# The username can consist only of letters, numbers, and underscore ("_").
from django.core.exceptions import ValidationError


def username_validator(value):
    for v in value:
        if not (v.isalpha() or v.isdigit() or v == "_"):
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
