# Generated by Django 4.1.7 on 2023-03-19 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0001_initial'),
        ('event', '0002_initial'),
        ('core', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.customer'),
        ),
        migrations.AddField(
            model_name='event',
            name='mutuals',
            field=models.ManyToManyField(related_name='mutualEvents', to='users.customer'),
        ),
        migrations.AddField(
            model_name='event',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.organization'),
        ),
        migrations.AddField(
            model_name='event',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.place'),
        ),
        migrations.AddField(
            model_name='digitalinvitationlog',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.customer'),
        ),
        migrations.AddField(
            model_name='digitalinvitationlog',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='event.event'),
        ),
        migrations.AddField(
            model_name='digitalinvitationlog',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='event.digitalinvitationtemplate'),
        ),
        migrations.AddField(
            model_name='digitalinvitation',
            name='audient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='event.targetedaudient'),
        ),
        migrations.AddField(
            model_name='digitalinvitation',
            name='log',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.digitalinvitationlog'),
        ),
        migrations.AddField(
            model_name='albumimage',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='event.album'),
        ),
        migrations.AddField(
            model_name='album',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='event.event'),
        ),
    ]
