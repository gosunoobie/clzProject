# Generated by Django 5.0.2 on 2024-03-28 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domestic_flights', '0017_alter_flightticket_issued_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightticket',
            name='issued_date',
            field=models.DateField(default='2024-03-28', max_length=50),
        ),
    ]
