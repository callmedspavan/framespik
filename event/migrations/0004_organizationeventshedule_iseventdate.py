# Generated by Django 4.1.7 on 2023-03-19 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationeventshedule',
            name='isEventDate',
            field=models.BooleanField(default=False),
        ),
    ]
