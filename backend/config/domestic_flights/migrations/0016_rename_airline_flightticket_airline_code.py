# Generated by Django 5.0.2 on 2024-03-27 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domestic_flights', '0015_flightticket_airline_flightticket_flight_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flightticket',
            old_name='airline',
            new_name='airline_code',
        ),
    ]
