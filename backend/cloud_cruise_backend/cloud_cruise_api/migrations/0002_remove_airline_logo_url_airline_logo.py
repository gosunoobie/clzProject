# Generated by Django 5.0.2 on 2024-02-25 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud_cruise_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airline',
            name='logo_url',
        ),
        migrations.AddField(
            model_name='airline',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='airline/'),
        ),
    ]