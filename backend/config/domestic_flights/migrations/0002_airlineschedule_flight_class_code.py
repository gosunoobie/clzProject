# Generated by Django 5.0.2 on 2024-03-19 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domestic_flights', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='airlineschedule',
            name='flight_class_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
