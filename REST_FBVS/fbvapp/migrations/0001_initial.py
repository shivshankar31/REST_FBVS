# Generated by Django 4.0.1 on 2022-02-02 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('Mark', models.DecimalField(decimal_places=2, max_digits=3)),
                ('Location', models.CharField(max_length=50)),
            ],
        ),
    ]
