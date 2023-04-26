# Generated by Django 4.2 on 2023-04-26 08:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
