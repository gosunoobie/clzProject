# Generated by Django 5.0.2 on 2024-03-27 11:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domestic_flights', '0011_transaction_guid'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FlightTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created date')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='modified date')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('issued_date', models.DateField(max_length=50)),
                ('arrival_destination', models.CharField(max_length=50)),
                ('departure_destination', models.CharField(max_length=50)),
                ('arrival_time', models.TimeField(blank=True, max_length=50, null=True)),
                ('pnr_no', models.CharField(max_length=50)),
                ('guid', models.CharField(blank=True, max_length=200, null=True)),
                ('booking', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='domestic_flights.booking')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
