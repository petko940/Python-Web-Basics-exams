from django.db import models
from django.db.models import Model


# Create your models here.

class Profile(Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image_url = models.URLField()


class Book(Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.URLField()
    type = models.CharField(max_length=30)
