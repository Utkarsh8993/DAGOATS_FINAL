# Generated by Django 4.1.5 on 2023-01-15 02:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_event_date_event_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(default=datetime.datetime(2023, 1, 15, 7, 46, 27, 734168)),
        ),
    ]
