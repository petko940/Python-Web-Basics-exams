from django.core.exceptions import ValidationError


def first_name_only_letter(value):
    if not value.isalpha():
        raise ValidationError("The name should contain only letters!")


def password_should_have_at_least_one_digit(value):
    if not any(char.isdigit() for char in value):
        raise ValidationError("The password must contain at least 1 digit!")
