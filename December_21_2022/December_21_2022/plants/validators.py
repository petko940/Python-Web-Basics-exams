from django.core.exceptions import ValidationError


def name_validation(value):
    if not (x for x in value if x.isalpha()):
        raise ValidationError("Plant name should contain only letters!")