from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Profile(models.Model):
    email = models.EmailField(unique=True)
    age = models.IntegerField(validators=[MinValueValidator(12)])
    password = models.CharField(max_length=30)
    first_name = models.CharField(verbose_name="First Name", max_length=30, blank=True)
    last_name = models.CharField(verbose_name="Last Name", max_length=30, blank=True)
    profile_picture = models.URLField(blank=True,
                                      verbose_name="Profile Picture")


class Game(models.Model):
    category = [
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Puzzle', 'Puzzle'),
        ('Strategy', 'Strategy'),
        ('Sports', 'Sports'),
        ('Board/Card Game', 'Board/Card Game'),
        ('Other', 'Other'),
    ]

    title = models.CharField(max_length=30, unique=True)
    category = models.CharField(max_length=15, choices=category)
    rating = models.FloatField(validators=[MinValueValidator(0.1), MaxValueValidator(5.0)])
    max_level = models.IntegerField(verbose_name='Max Level', blank=True, null=True, validators=[MinValueValidator(1)])
    image_url = models.URLField(verbose_name='Image URL')
    summary = models.TextField(blank=True, null=True)
