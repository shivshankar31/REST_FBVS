# Generated by Django 4.0.1 on 2022-02-05 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbvapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='Mark',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]