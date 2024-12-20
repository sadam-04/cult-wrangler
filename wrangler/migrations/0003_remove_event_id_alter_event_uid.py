# Generated by Django 5.1.4 on 2024-12-12 05:25

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wrangler', '0002_event_uid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='id',
        ),
        migrations.AlterField(
            model_name='event',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
