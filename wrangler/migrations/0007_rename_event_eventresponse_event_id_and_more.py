# Generated by Django 5.1.4 on 2024-12-13 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wrangler', '0006_event_creator'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventresponse',
            old_name='event',
            new_name='event_id',
        ),
        migrations.RenameField(
            model_name='eventresponse',
            old_name='times',
            new_name='responses',
        ),
    ]
