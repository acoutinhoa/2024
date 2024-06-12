# Generated by Django 4.2.11 on 2024-06-03 22:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1850), django.core.validators.MaxValueValidator(2050)])),
                ('mes', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(12)])),
                ('dia', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(31)])),
            ],
        ),
    ]