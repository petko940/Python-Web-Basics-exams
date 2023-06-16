from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Game(models.Model):
    CHOICES = (
        ('Action', 'Action'),
        ("Adventure", "Adventure"),
        ("Puzzle", "Puzzle"),
        ("Strategy", "Strategy"),
        ("Sports", "Sports"),
        ("Board/Card Game", "Board/Card Game"),
        ("Other", "Other")
    )

    title = models.CharField(
        max_length=30,
        unique=True)

    category = models.CharField(
        max_length=15,
        choices=CHOICES)

    rating = models.FloatField(
        validators=[MinValueValidator(0.1), MaxValueValidator(5)])

    max_level = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1)])

    image_url = models.URLField()

    summary = models.TextField(
        blank=True,
        null=True)
