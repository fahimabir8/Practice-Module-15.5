# Generated by Django 5.0.6 on 2024-06-26 00:20

import phone_field.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Musician', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicianmodel',
            name='phone_no',
            field=phone_field.models.PhoneField(max_length=11, unique=True),
        ),
    ]
