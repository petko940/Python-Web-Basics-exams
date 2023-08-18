# Generated by Django 4.2.4 on 2023-08-18 10:59

import August_2023_Retake_Eventer.events.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Event Name')),
                ('category', models.CharField(choices=[('Sports', 'Sports'), ('Festivals', 'Festivals'), ('Conferences', 'Conferences'), ('Performing Art', 'Performing Art'), ('Concerts', 'Concerts'), ('Theme Party', 'Theme Party'), ('Other', 'Other')])),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True, validators=[August_2023_Retake_Eventer.events.validators.prevent_date_earlier_than_today])),
                ('event_image', models.URLField(verbose_name='Event Image')),
            ],
        ),
    ]