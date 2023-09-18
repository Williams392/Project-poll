# Generated by Django 4.2.1 on 2023-09-18 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_eventtypeoptions_statusoptions_visibiltyoptions_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='contribution',
        ),
        migrations.RemoveField(
            model_name='events',
            name='event_type',
        ),
        migrations.RemoveField(
            model_name='events',
            name='present',
        ),
        migrations.RemoveField(
            model_name='events',
            name='state',
        ),
        migrations.RemoveField(
            model_name='interested',
            name='interested',
        ),
        migrations.AddField(
            model_name='events',
            name='e_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='events.eventtypeoptions'),
        ),
        migrations.AddField(
            model_name='events',
            name='event_banner',
            field=models.ImageField(blank=True, null=True, upload_to='event_banners/'),
        ),
        migrations.AddField(
            model_name='events',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='events.statusoptions'),
        ),
        migrations.AddField(
            model_name='events',
            name='visibility',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='events.visibiltyoptions'),
        ),
        migrations.AlterField(
            model_name='events',
            name='location',
            field=models.CharField(max_length=350),
        ),
    ]
