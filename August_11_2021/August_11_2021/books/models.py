from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.URLField()
    type = models.CharField(max_length=30)
