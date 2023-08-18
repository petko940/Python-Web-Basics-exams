from django.core.validators import MinLengthValidator
from django.db import models
from .validators import prevent_date_earlier_than_today


# Create your models here.
class EventModel(models.Model):
    event_name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2)
        ],
        verbose_name="Event Name"
    )
    category = models.CharField(
        choices=[
            ("Sports", "Sports"),
            ("Festivals", "Festivals"),
            ("Conferences", "Conferences"),
            ("Performing Art", "Performing Art"),
            ("Concerts", "Concerts"),
            ("Theme Party", "Theme Party"),
            ("Other", "Other")
        ]
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    date = models.DateField(
        blank=True,
        null=True,
        validators=[
            prevent_date_earlier_than_today
        ]
    )
    event_image = models.URLField(
        verbose_name="Event Image",
    )
