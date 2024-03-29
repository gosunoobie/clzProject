# Generated by Django 5.0.2 on 2024-03-19 11:16

import core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterOTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created date')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='modified date')),
                ('otp', models.CharField(max_length=6)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name of Wallet')),
                ('photo', models.ImageField(upload_to='wallet_photo', validators=[core.validators.validate_file_size])),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='account_provider',
            field=models.CharField(default='CloudCruise', max_length=50),
        ),
        migrations.CreateModel(
            name='BankDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField(verbose_name='Priority')),
                ('account_number', models.CharField(max_length=50, verbose_name='Account Number')),
                ('account_holder_name', models.CharField(max_length=50, verbose_name='Account Holder Name')),
                ('bank_name', models.CharField(max_length=50, verbose_name='Bank Name')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User having this account')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentWallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField(verbose_name='Priority')),
                ('wallet_id', models.CharField(max_length=50, verbose_name='Wallet Id')),
                ('wallet_holder_name', models.CharField(max_length=50, verbose_name='Wallet Holder name')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User having this Wallet')),
                ('wallet_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.wallet', verbose_name='Available Wallet')),
            ],
        ),
        migrations.AddConstraint(
            model_name='bankdetail',
            constraint=models.UniqueConstraint(fields=('user', 'priority'), name='bank_priority_constraint'),
        ),
        migrations.AddConstraint(
            model_name='bankdetail',
            constraint=models.UniqueConstraint(fields=('user', 'account_number'), name='bank_number_constraint'),
        ),
        migrations.AddConstraint(
            model_name='paymentwallet',
            constraint=models.UniqueConstraint(fields=('user', 'priority'), name='wallet_priority_constraint'),
        ),
        migrations.AddConstraint(
            model_name='paymentwallet',
            constraint=models.UniqueConstraint(fields=('user', 'wallet_id'), name='wallet_id_constraint'),
        ),
    ]
