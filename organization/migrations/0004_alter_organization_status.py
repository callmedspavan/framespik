# Generated by Django 4.1.7 on 2023-03-19 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_alter_organization_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('H', 'Hold'), ('I', 'In Active')], default='A', max_length=1),
        ),
    ]