# Generated by Django 4.2 on 2023-04-26 15:57

import django.core.validators
from django.db import migrations, models
import plants.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_type', models.CharField(choices=[('Outdoor Plants', 'Outdoor Plants'), ('Indoor Plants', 'Indoor Plants')], max_length=14)),
                ('name', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2), plants.models.name_validator])),
                ('image_url', models.URLField(verbose_name='Image URL')),
                ('description', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
    ]