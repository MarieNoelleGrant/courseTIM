# Generated by Django 3.0.4 on 2020-03-10 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('particpants', '0002_auto_20200305_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='date_naissance',
            field=models.DateField(),
        ),
    ]
