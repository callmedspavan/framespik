# Generated by Django 4.1.7 on 2023-03-20 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0009_remove_organization_proprietorimageurl_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='status',
            field=models.CharField(choices=[('I', 'In Active'), ('A', 'Active'), ('H', 'Hold')], default='A', max_length=1),
        ),
    ]
