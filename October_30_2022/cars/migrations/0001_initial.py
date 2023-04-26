# Generated by Django 4.2 on 2023-04-26 08:08

import cars.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('sports_car', 'Sports Car'), ('pickup', 'Pickup'), ('crossover', 'Crossover'), ('minibus', 'Minibus'), ('other', 'Other')], max_length=10)),
                ('model', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2)])),
                ('year', models.IntegerField(validators=[cars.models.validate_year])),
                ('image_url', models.URLField(verbose_name='Image URL')),
                ('price', models.FloatField(validators=[django.core.validators.MinLengthValidator(1)])),
            ],
        ),
    ]
