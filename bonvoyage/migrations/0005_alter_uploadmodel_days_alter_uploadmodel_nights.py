# Generated by Django 4.1.6 on 2023-02-08 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonvoyage', '0004_userregmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadmodel',
            name='days',
            field=models.CharField(choices=[('day', 'day'), ('1-day', '1-day'), ('2-day', '2-day'), ('3-day', '3-day'), ('4-day', '4-day'), ('5-day', '5-day'), ('6-day', '6-day'), ('7-day', '7-day')], max_length=30),
        ),
        migrations.AlterField(
            model_name='uploadmodel',
            name='nights',
            field=models.CharField(choices=[('night', 'night'), ('1-night', '1-night'), ('2-night', '2-night'), ('3-night', '3-night'), ('4-night', '4-night'), ('5-night', '5-night'), ('6-night', '6-night'), ('7-night', '7-night')], max_length=30),
        ),
    ]
