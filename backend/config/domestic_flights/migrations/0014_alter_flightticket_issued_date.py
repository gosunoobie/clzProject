# Generated by Django 5.0.2 on 2024-03-27 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domestic_flights', '0013_booking_for_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightticket',
            name='issued_date',
            field=models.DateField(max_length=50, null=True),
        ),
    ]