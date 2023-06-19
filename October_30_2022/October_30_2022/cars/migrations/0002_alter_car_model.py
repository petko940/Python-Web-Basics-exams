# Generated by Django 4.2.2 on 2023-06-19 09:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinValueValidator(2)]),
        ),
    ]
