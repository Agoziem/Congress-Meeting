# Generated by Django 2.2 on 2024-07-08 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0004_programme_venue'),
    ]

    operations = [
        migrations.AddField(
            model_name='programme',
            name='year',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
