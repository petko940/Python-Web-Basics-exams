# Generated by Django 4.2 on 2023-04-26 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_car_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='type',
            field=models.CharField(choices=[('sports car', 'Sports Car'), ('pickup', 'Pickup'), ('crossover', 'Crossover'), ('minibus', 'Minibus'), ('other', 'Other')], max_length=10),
        ),
    ]
